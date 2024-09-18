import aiohttp
from pydantic import parse_obj_as
from sqlalchemy import text

from config import ExtractConfig, Settings
from database import DB
from models import ImportedLeaveInformation
from pipeline.schema import ImportedLeaveInformationSchema


class Extract:
    def __init__(self, config: Settings, db: DB, logger):
        self.db = db
        self.config = config
        self.logger = logger

    async def fetch_records_from_api(self, api_url: str, bearer_token: str, batch_size: int, page: int) -> dict:
        query_params = {
            "fetchType": "all",
            "startDate": ExtractConfig.START_DATE.value,
            "endDate": ExtractConfig.END_DATE.value,
            "size": batch_size,
            "roleType": "issuer",
            "page": page,
        }

        headers = {"Authorization": f"Bearer {bearer_token}"}
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, headers=headers, params=query_params) as response:
                if response.status == 200:
                    payload = await response.json()
                    return payload
                else:
                    self.logger.error(f"Request failed with status code {response.status}")

    async def run_extraction(self) -> None:
        """
        Fetch data from API and store to raw flatfile asynchronously.
        """
        page = 1
        batch_size = ExtractConfig.BATCH_SIZE.value
        total_fetched_data_size = 0
        api_url = self.config.source_api_endpoint
        bearer_token = self.config.auth_bearer_token

        await self.truncate_table()

        while True:
            payload = await self.fetch_records_from_api(api_url, bearer_token, batch_size, page)
            total_data_size = payload.get("meta", {}).get("total", 0)
            fetched_data_size = payload.get("meta", {}).get("size", 0)

            # batch insertion
            leave_records = parse_obj_as(list[ImportedLeaveInformationSchema], payload["data"])
            self.logger.info(f"Inserted {fetched_data_size} records.")
            await self.insert_into_raw_flatfile(leave_records)

            page += 1
            total_fetched_data_size += fetched_data_size

            if total_data_size == 0:
                break

    async def insert_into_raw_flatfile(self, leave_records: list[ImportedLeaveInformationSchema]) -> None:
        """
        Insert record into raw flatfile table asynchronously.
        """
        with self.db.session_scope() as session:
            for leave_record in leave_records:
                #print(leave_record)
                record = ImportedLeaveInformation(**leave_record.dict())
                session.add(record)
            self.logger.info("[EXTRACT] Record extracted successfully.")

    async def truncate_table(self) -> None:
        """
        Truncate the raw flatfile table before inserting data.
        """
        with self.db.session_scope() as session:
            session.execute(text("TRUNCATE TABLE raw.imported_leave_information"))
            session.commit()  # Ensure truncation is committed
            self.logger.info("[TRUNCATE] Table truncated successfully.")
