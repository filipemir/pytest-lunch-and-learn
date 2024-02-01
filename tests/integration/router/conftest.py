import pytest
from fastapi.testclient import TestClient
from psycopg import AsyncConnection

from app.main import app
from app.db import get_db_connection


@pytest.fixture
async def test_client(test_db_connection: AsyncConnection) -> TestClient:
    app.dependency_overrides[get_db_connection] = lambda: test_db_connection
    return TestClient(app)
