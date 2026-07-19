from openai import OpenAI

from app.core.config import settings

from app.prompts.manager import (
    get_customer_service_prompt
)


client = OpenAI(
    api_key=settings.deepseek_api_key,
    base_url=settings.deepseek_base_url
)



def chat_with_llm(
    message,
    history=None
):

    if history is None:

        history=[]

    messages=[

    {
    "role":"system",
    "content":
    get_customer_service_prompt()
    }

    ]


    messages.extend(history)


    messages.append({

    "role":"user",

    "content":message

    })


    response=client.chat.completions.create(

    model=settings.deepseek_model,

    messages=messages,

    temperature=0.2

    )


    return response.choices[0].message.content