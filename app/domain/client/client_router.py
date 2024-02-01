from fastapi import Depends, APIRouter

from app.domain.client.client_models import Client
from app.domain.client.client_service import ClientService

router = APIRouter()


@router.get(
    "/clients",
    response_model=list[Client],
)
async def get_clients(
    client_svc: ClientService = Depends(),
):
    return await client_svc.get_clients()
