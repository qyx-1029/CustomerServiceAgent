from openai import OpenAI

from app.core.config import settings

from app.prompts.manager import (
    get_customer_service_prompt
)


client = OpenAI(
    api_key=settings.deepseek_api_key,
    base_url=settings.deepseek_base_url
)



def chat_with_llm(message:str):


    system_prompt = (
        get_customer_service_prompt()
    )


    response = client.chat.completions.create(

        model=settings.deepseek_model,


        messages=[

            {
                "role":"system",
                "content":system_prompt
            },


            {
                "role":"user",
                "content":message
            }

        ],

        temperature=0.2

    )


    return response.choices[0].message.content