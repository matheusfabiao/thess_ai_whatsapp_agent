from agno.db.postgres import PostgresDb
from agno.db.sqlite import SqliteDb

from config import settings


class MemoryService:
    def __init__(self):
        self.__db_url = settings.DATABASE_CONNECTION_URI

    def get_memory_db(self) -> PostgresDb:
        return PostgresDb(
            db_url=self.__db_url,
        )

    @staticmethod
    def get_test_memory_db() -> SqliteDb:
        # TODO: Remover na primeira versão estável
        return SqliteDb(
            db_url='sqlite:///db.sqlite3',
        )
