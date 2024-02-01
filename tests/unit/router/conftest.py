import pytest
from typing import Callable
from unittest.mock import AsyncMock
from fastapi.testclient import TestClient


from app.db import get_db_connection
from app.main import app


@pytest.fixture
def test_client(
    get_mock_db_connection: Callable[[], AsyncMock]
) -> TestClient:
    app.dependency_overrides[get_db_connection] = get_mock_db_connection

    return TestClient(app)
