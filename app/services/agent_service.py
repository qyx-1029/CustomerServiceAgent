from app.agent.graph import agent_graph

from app.memory.memory_manager import (
    save_message,
    get_history
)



def process_user_message(
    user_id,
    message
):


    

    # 1. 先读取历史
    history=get_history(
        user_id
    )

    # 2. 调用Agent
    result=agent_graph.invoke({

        "user_id":user_id,

        "message":message,

        "history":history

    })


    reply=result["response"]


    # 3. 保存用户消息
    save_message(

        user_id,

        "user",

        message

    )


    # 4. 保存AI回复
    save_message(

        user_id,

        "assistant",

        reply

    )


    return {

        "reply":reply,

        "intent":
        result["intent"]

    }
