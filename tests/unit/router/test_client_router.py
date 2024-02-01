from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient

from app.domain.client.client_service import ClientService

"""
These are tests that hit our router methods but instead of hitting them directly
we use FastAPI's TestClient, so they aren't strictly unit tests. This approach
give us confidence above and beyond what we get from just testing the router
methods directly that requests are routed to our router files in the the way
that we expect and triggering all the middleware we expect (i.e. the URL matches
our expectation,auth works as expected, etc.). Code below the router should be mocked
out
"""


@patch.object(
    ClientService,
    "get_clients",
    return_value=[],
)
async def test_get_clients(mock_svc_get_clients: MagicMock, test_client: TestClient):
    response = test_client.get("/clients")

    assert response.status_code == 200

    mock_svc_get_clients.assert_called_once()
