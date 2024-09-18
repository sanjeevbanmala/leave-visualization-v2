import asyncio

from loguru import logger

from config import Settings, SqlDirPaths
from database import DB
from pipeline.extract import Extract
from pipeline.transform_load import TransformLoad


class DataPipeline:
    def __init__(self):
        self.config: Settings = Settings()
        self.logger = logger
        self.db = DB(config=self.config, logger=self.logger)

    def run_pipeline(self):
        extract = Extract(config=self.config, db=self.db, logger=self.logger)
        asyncio.run(extract.run_extraction())

        # transform_load = TransformLoad(db=self.db, logger=logger)
        # transform_load.run_sql_scripts(
        #     sql_dir=SqlDirPaths.TRANSFORM_SQL_DIR,
        # )
        # transform_load.run_sql_scripts(
        #     sql_dir=SqlDirPaths.LOAD_SQL_DIR,
        # )


if __name__ == "__main__":
    data_pipeline = DataPipeline()
    data_pipeline.run_pipeline()
