from typing import Any
from fastapi import Depends
from psycopg import AsyncConnection
from psycopg.rows import class_row

from app.db import get_db_connection
from app.domain.client.client_models import Client


class ClientDao:
    def __init__(
        self,
        connection: AsyncConnection[Any] = Depends(get_db_connection),
    ):
        self.connection = connection

    async def get_clients(self) -> list[Client]:
        async with self.connection.cursor(row_factory=class_row(Client)) as cursor:
            await cursor.execute(query="SELECT * FROM clients")
            return await cursor.fetchall()
