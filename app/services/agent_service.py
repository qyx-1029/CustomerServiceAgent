from app.services.llm_service import chat_with_llm



def process_user_message(
        user_id:str,
        message:str
):


    reply = chat_with_llm(
        message
    )


    return {

        "user_id":user_id,

        "reply":reply

    }