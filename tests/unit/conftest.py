import pytest
from unittest.mock import AsyncMock


@pytest.fixture
def mock_db():
    return AsyncMock()


@pytest.fixture
def get_mock_db_connection(mock_db: AsyncMock):
    def getter():
        return mock_db

    return getter

