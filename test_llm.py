from app.services.llm_service import chat_with_llm


result = chat_with_llm(
    "你是谁？"
)


print(result)