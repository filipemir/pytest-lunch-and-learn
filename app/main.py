from fastapi import FastAPI

from app.domain.client.client_router import router as client_router

app = FastAPI()


app.include_router(client_router)
