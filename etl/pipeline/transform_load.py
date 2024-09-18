import os

from database.database import DB
from sqlalchemy import text


class TransformLoad:
    def __init__(self, db: DB, logger):
        self.db = db
        self.logger = logger

    def run_sql_scripts(self, sql_dir: str) -> None:
        sql_file_path = os.listdir(sql_dir)

        for file_name in sorted(sql_file_path):
            sql_file_path = os.path.join(sql_dir, file_name)

            with open(sql_file_path, "r") as file:
                query = "".join(file.readlines())

                with self.db.session_scope() as session:
                    session.execute(text(query))

            self.logger.info(f"Successfully executed {file_name}.")
