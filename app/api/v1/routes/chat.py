from fastapi import APIRouter

from app.schemas.chat import ChatRequest

from app.schemas.common import ApiResponse

from app.services.agent_service import process_user_message



router=APIRouter()



@router.post("/chat")
def chat(
    request:ChatRequest
):


    result = process_user_message(

        request.user_id,

        request.message

    )


    return ApiResponse(

        data=result

    )