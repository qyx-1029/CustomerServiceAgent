from fastapi import APIRouter
from app.schemas.common import ApiResponse

router = APIRouter()


@router.get("/health", response_model=ApiResponse)
def health_check():
    return ApiResponse(
        code=0,
        message="service is healthy",
        data={"status": "ok"}
    )