import json

from app.memory.redis_client import redis_client

# 最大保存对话数量
MAX_HISTORY = 20

def get_memory_key(user_id):

    return f"chat:{user_id}"



def save_message(
    user_id,
    role,
    content
):


    key=get_memory_key(user_id)


    history=[]


    data=redis_client.get(key)


    if data:

        history=json.loads(data)



    history.append({

        "role":role,

        "content":content

    })


    # ==========================
    # Memory限制
    # ==========================

    history = history[-MAX_HISTORY:]



    redis_client.set(

        key,

        json.dumps(history),

        ex=3600

    )



def get_history(user_id):


    key=get_memory_key(user_id)


    data=redis_client.get(key)


    if not data:

        return []


    return json.loads(data)
