from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1 import api_router


setup_logging()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)


app.include_router(
    api_router,
    prefix="/api/v1"
)


@app.get("/")
def root():

    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "status": "running"
    }