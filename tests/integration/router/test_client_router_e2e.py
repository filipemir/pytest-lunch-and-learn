from fastapi.testclient import TestClient

from app.domain.client.client_models import Client

"""
The router integration tests are end-to-end tests of our API. They hit
every layer of the application. They can give us enormous confidence that
our application is working as expected, but they're also slow and complex
to write. While we used them quite a bit early on when it was pretty much
the only type of BE testing we had, we should now use them pretty sparingly
and typically supplementary to units tests and DAO tests
"""

def test_get_clients_endpoint(
    test_client: TestClient,
    client_1: Client,
    client_2: Client
):
    response = test_client.get("/clients")
    assert response.status_code == 200

    payload = response.json()

    assert len(payload) == 2
