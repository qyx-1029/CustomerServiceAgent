from openai import OpenAI

from app.core.config import settings



client = OpenAI(
    api_key=settings.deepseek_api_key,
    base_url=settings.deepseek_base_url
)



def chat_with_llm(message:str):

    response = client.chat.completions.create(

        model=settings.deepseek_model,

        messages=[

            {
                "role":"system",
                "content":
                """
                你是一名专业客服。

                要求：
                1.回答用户问题
                2.保持礼貌
                3.不要编造信息
                4.回答简洁
                """
            },


            {
                "role":"user",
                "content":message
            }

        ],

        temperature=0.3

    )


    return response.choices[0].message.content