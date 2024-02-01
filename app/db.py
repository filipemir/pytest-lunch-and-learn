from typing import AsyncGenerator, Any
from psycopg import AsyncConnection

from app.config import config


async def get_db_connection() -> AsyncGenerator[AsyncConnection[Any], None]:
    async with await AsyncConnection.connect(config.DATABASE_URL) as connection:
        yield connection
