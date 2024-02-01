import pytest
from typing import AsyncGenerator, Callable, Coroutine, Any
from psycopg import AsyncConnection
from psycopg.rows import class_row, Row

from app.domain.client.client_models import Client


@pytest.fixture
async def test_db_connection() -> AsyncGenerator[AsyncConnection, None]:
    async with await AsyncConnection.connect(
        "postgres://postgres:postgres@db:5439/db_test?sslmode=disable"
    ) as connection:
        yield connection


@pytest.fixture
async def client_factory(
    test_db_connection: AsyncConnection[Row],
) -> Callable[[int, str, str, str, str], Coroutine[Any, Any, Client]]:
    async def create_client(
        id: int,
        name: str,
    ):
        query = f"""
            INSERT INTO clients (
                id,
                name
            ) VALUES (
                '{id}',
                '{name}'
            ) RETURNING *;
        """
        async with test_db_connection.cursor(row_factory=class_row(Client)) as cursor:
            await cursor.execute(query)
            return await cursor.fetchone()

    yield create_client

    async with test_db_connection.cursor() as cursor:
        await cursor.execute(
            query="TRUNCATE clients CASCADE;",
        )


@pytest.fixture
async def client_1(
    client_factory: Callable[..., Coroutine[Any, Any, Client]],
):
    return await client_factory(
        id=1,
        name="Charlie",
    )


@pytest.fixture
async def client_2(
    client_factory: Callable[..., Coroutine[Any, Any, Client]],
):
    return await client_factory(
        id=2,
        name="Dougie",
    )
