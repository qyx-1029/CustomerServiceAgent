from app.agent.state import AgentState
from app.services.llm_service import chat_with_llm
from app.tools.order_tool import query_order
from app.tools.price_tool import query_price
from app.tools.human_tool import transfer_human
from app.memory.session_manager import (
    save_session,
    get_session
)


def intent_node(state):


    user_id=state["user_id"]

    message=state["message"]


    session=get_session(user_id)


    # 如果正在等待订单号

    if session.get(
        "task"
    )=="query_order":


        state["intent"]="order"


        return state

    history=state.get(
        "history",
        []
    )


    history_text=""


    for item in history[-6:]:

        history_text += item["content"]

    context = history_text + message



    if "订单" in message:

        state["intent"]="order"


    elif "价格" in message:

        state["intent"]="price"


    elif "人工" in message:

        state["intent"]="human"


    else:

        state["intent"]="chat"


    return state



def chat_node(
        state:AgentState
):


    response = chat_with_llm(
        state["message"],

        state["history"]
    )


    state["response"]=response


    return state



def order_node(state):


    user_id = state["user_id"]

    message = state["message"]


    session=get_session(user_id)


    # 已经等待订单号

    if session.get("status")=="waiting_order_id":


        order_id=message


        result=query_order(order_id)


        save_session(

            user_id,

            {

                "task":"query_order",

                "status":"completed",

                "order_id":order_id
            
            }

        )


        state["response"]=result


    elif session.get("status")=="completed":


        order_id=session.get(
            "order_id"
        )


        result=query_order(order_id)


        state["response"]=result



    else:


        save_session(

            user_id,

            {
                "task":"query_order",

                "status":
                "waiting_order_id"

            }

        )


        state["response"]=(
            "好的，请提供您的订单号。"
        )

    return state



def price_node(state):


    result=query_price(
        "机器人"
    )


    state["tool_result"]=result


    state["response"]=result


    return state



def human_node(state):


    result=transfer_human(
        "用户请求"
    )


    state["response"]=result


    return state

