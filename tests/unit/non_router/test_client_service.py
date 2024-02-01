from unittest.mock import AsyncMock

import pytest

from app.domain.client.client_service import ClientService


@pytest.fixture
def client_dao_mock():
    return AsyncMock(
        get_clients=AsyncMock(return_value=[1, 2, 3])
    )


@pytest.fixture
def system_under_test(client_dao_mock: AsyncMock):
    return ClientService(dao=client_dao_mock)


async def test_get_clients(
    system_under_test: ClientService,
    client_dao_mock: AsyncMock
):
    result = await system_under_test.get_clients()

    client_dao_mock.get_clients.assert_called_once()
    assert result == [1, 2, 3]

