from typing import TypedDict


class AgentState(TypedDict):

    user_id:str

    message:str

    intent:str

    task_status:str

    order_id:str

    tool_result:str

    response:str

    history:list


