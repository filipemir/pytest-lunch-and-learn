import pytest
from psycopg import AsyncConnection
from psycopg.rows import Row

from app.domain.client.client_dao import ClientDao
from app.domain.client.client_models import Client

"""
Unit testing DAOs is not worth anyone's time. The only way to reliably
test DAOs is to run them against a real database, which means they'll be slower
and have a more complicated setup than our unit tests. As such, keeping the surface
are of DAOs very small is really helpful. DAO methods should just execute SQL
queries. Everything else should go in another layer

These tests use factory fixtures, a really reusable pattern to generate test
data for integration tests. They allow you to encapsulate the logic for record
creation AND cleanup in one fixture, making it really easy to ensure that your
tests ALWAYS clean up after themselves
"""


@pytest.fixture
def system_under_test(test_db_connection: AsyncConnection[Row]):
    return ClientDao(connection=test_db_connection)


async def test_get_two_clients(
    system_under_test: ClientDao,
    client_1: Client,
    client_2: Client
):
    """
    By invoking both fixtures we're inserting two clients into the database,
    and can assert that the DAO method responds accordingly
    """
    results = await system_under_test.get_clients()

    assert len(results) == 2


async def test_get_one_client(
    system_under_test: ClientDao,
    client_1: Client
):
    """
    Note that here we're only expecting one client, even though this test
    will generally run after the previous one, demonstrating the self-cleanup
    nature of the factory AND that each fixture only inserts one record
    """
    results = await system_under_test.get_clients()

    assert len(results) == 1



