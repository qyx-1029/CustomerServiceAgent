from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.common import ApiResponse

router = APIRouter()


class ChatRequest(BaseModel):
    user_id: str
    message: str


@router.post("/chat", response_model=ApiResponse)
def chat(request: ChatRequest):
    return ApiResponse(
        code=0,
        message="chat endpoint ready",
        data={
            "user_id": request.user_id,
            "reply": "这里是客服回复入口，下一阶段接入大模型。"
        }
    )