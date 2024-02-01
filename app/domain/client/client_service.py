from fastapi import Depends

from app.domain.client.client_dao import ClientDao
from app.domain.client.client_models import Client
from app.gateway import ThirdPartyGateway


class ClientService:
    def __init__(self, dao: ClientDao = Depends()):
        self.dao = dao

    async def get_clients(self) -> list[Client]:
        thing = await ThirdPartyGateway().get_a_thing(thing_id="abc123")
        print(thing)
        return await self.dao.get_clients()
