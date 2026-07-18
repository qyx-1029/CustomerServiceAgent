from fastapi import APIRouter
from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.chat import router as chat_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["Health"])
api_router.include_router(chat_router, tags=["Chat"])