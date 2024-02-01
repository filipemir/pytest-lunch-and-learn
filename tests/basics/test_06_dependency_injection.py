from unittest.mock import AsyncMock

import pytest

from app.domain.client.client_service import ClientService

"""
Patching is great and all but Dependency Injection beats Patching every time
"""

@pytest.fixture
def client_dao():
    return AsyncMock()


@pytest.fixture
def system_under_test(client_dao: AsyncMock):
    """
    One of the great virtues of dependency injection as a pattern is that it
    makes testing way easier than it might otherwise be. You don't need to
    patch anything: simply pass in a mock object and you're good to go! FastAPI's
    happy path is to use dependency injection, and when we stay in that path
    testing is much easier.

    In the past I've seen instances of us defining these monster mock classes
    that are essentially dumbed down versions of the classes we use, that then
    have to be kept in sync with the real thing in perpetuity. They are also
    really hard to modify for the purpose of specific tests.
    """
    return ClientService(dao=client_dao)


async def test_get_client(system_under_test: ClientService, client_dao: AsyncMock):
    # Notice that if all you care about is that the method is returning
    # the same thing that a dependency is returning, you don't even need
    # to return the same type of object
    client_dao.get_clients = AsyncMock(return_value="wow-nelly")

    result = await system_under_test.get_clients()

    client_dao.get_clients.assert_called_once()
    assert result == "wow-nelly"
