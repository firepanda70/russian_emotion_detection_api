from fastapi import FastAPI

from endpoints import router
from config import settings


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description
)

app.include_router(router)
