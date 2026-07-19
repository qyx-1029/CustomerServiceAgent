import json

from app.memory.redis_client import redis_client



def save_session(user_id,data):

    key=f"session:{user_id}"

    redis_client.set(

        key,

        json.dumps(data),

        ex=3600

    )



def get_session(user_id):

    key=f"session:{user_id}"

    data=redis_client.get(key)


    if data:

        return json.loads(data)


    return {}