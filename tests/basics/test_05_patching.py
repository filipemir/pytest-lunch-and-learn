from unittest.mock import AsyncMock, MagicMock
from unittest import mock

import pytest

from app.domain.client.client_service import ClientService
from app.gateway import ThirdPartyGateway

"""
There are a number of ways of patching code. Which you use is
largely a matter of preference, as they mostly are different
ways to call on the same underlying mechanism
"""


async def test_patching_with_unittest_mock():
    """
    You can use the native unittest's mock function as a context manager.
    The most common trip up here is that we typically want to provide the
    name of the module as we import it in the code (i.e.
    "app.utils.to_query_param_str" in this example). That doesn't work.
     You need to patch the object in the module that is using it and where you
     want it patched
    """
    with mock.patch("app.gateway.to_query_param_str") as mock_util:
        gateway = ThirdPartyGateway()

        await gateway.get_a_thing(thing_id="abc123")

        mock_util.assert_called_once_with(param_name="thing_id", param_values=["abc123"])


@mock.patch("app.gateway.to_query_param_str")
async def test_patching_with_patch_annotation(mock_util: MagicMock):
    """
    You can also use the native unittest's mock function as an annotation.
    Works exactly the same, except that the mock is exposed to you via a fixture.
    This is a nice way to keep the definition of the mocks outside the
    body of the tests, but it can get unwieldy when you have lots of patched
    objects
    """
    gateway = ThirdPartyGateway()

    await gateway.get_a_thing(thing_id="abc123")

    mock_util.assert_called_once_with(param_name="thing_id", param_values=["abc123"])


@pytest.fixture
def mock_util_from_fixture():
    with mock.patch("app.gateway.to_query_param_str") as mock_util:
        yield mock_util


async def test_patching_with_custom_patching_fixture(mock_util_from_fixture: MagicMock):
    """
    A better way when you have lots of patched objects is to define
     the patching fixtures yourself
    """
    gateway = ThirdPartyGateway()

    await gateway.get_a_thing(thing_id="abc123")

    mock_util_from_fixture.assert_called_once_with(param_name="thing_id", param_values=["abc123"])


async def test_patching_with_mocker(mocker: MagicMock):
    """
    We also have the mocker fixture, which is made available to us
    via the pytest-mock package. It's just a thin wrapper around
    the native unittest's mock function, so it works the same
    """
    mock_util = mocker.patch("app.gateway.to_query_param_str")
    gateway = ThirdPartyGateway()

    await gateway.get_a_thing(thing_id="abc123")

    mock_util.assert_called_once_with(param_name="thing_id", param_values=["abc123"])


@mock.patch("app.gateway.to_query_param_str")
async def test_patching_with_return_value(mock_util: MagicMock):
    """
    You can specify return values for your mocks
    """
    mock_util.return_value = "?foo=bar"

    gateway = ThirdPartyGateway()

    result = await gateway.get_a_thing(thing_id="abc123")

    assert result["query_string"] == "?foo=bar"


@mock.patch("app.gateway.to_query_param_str")
async def test_patching_with_side_effect(mock_util: MagicMock):
    """
    Instead of specifying a return_value you can also specify a
    side_effect, to replace the implementation of a method
    """
    def return_empty_list(param_name: str, param_values: list[str]):
        return "?foo=bar"

    mock_util.side_effect = return_empty_list

    gateway = ThirdPartyGateway()

    result = await gateway.get_a_thing(thing_id="abc123")

    assert result["query_string"] == "?foo=bar"


@mock.patch("app.domain.client.client_service.ClientDao")
@mock.patch.object(
    ThirdPartyGateway,
    "get_a_thing",
    return_value={"thing": "thong"}
)
async def test_patching_class_method(mock_gateway: MagicMock, _mock_dao: AsyncMock):
    """
    For patching methods on a class instance, using `patch.object` can be cleaner.
    You can also use in all the ways we've used above (annotation, context manager,
    fixture, mocker fixture)
    """
    system_under_test = ClientService(dao=AsyncMock(return_value=[]))

    await system_under_test.get_clients()

    mock_gateway.assert_called_once_with(thing_id="abc123")

