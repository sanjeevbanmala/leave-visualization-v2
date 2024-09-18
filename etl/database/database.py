from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Settings


class DB:
    def __init__(self, config: Settings, logger):
        self.config = config
        self.logger = logger
        self.engine = create_engine(self.get_connection_url(), echo_pool=True, pool_size=50, pool_pre_ping=True)

    def get_connection_url(self) -> str:
        host = self.config.db_host_name
        username = self.config.db_username
        password = self.config.db_password
        db_name = self.config.db_name
        port = self.config.db_port

        return f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"

    @contextmanager
    def session_scope(self):
        Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        session_local = Session()
        self.logger.info("Fetching session.")
        try:
            yield session_local
            session_local.commit()
        except Exception as e:
            session_local.rollback()
            raise e
        finally:
            session_local.close()
            self.logger.info("DB session closed.")


__all__ = ["DB"]
