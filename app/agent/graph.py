from langgraph.graph import (
    StateGraph,
    END
)

from app.agent.state import AgentState

from app.agent.nodes import *

from app.agent.router import router



workflow=StateGraph(
    AgentState
)


workflow.add_node(
    "intent",
    intent_node
)


workflow.add_node(
    "order",
    order_node
)


workflow.add_node(
    "price",
    price_node
)


workflow.add_node(
    "human",
    human_node
)


workflow.add_node(
    "chat",
    chat_node
)



workflow.set_entry_point(
    "intent"
)


workflow.add_conditional_edges(

    "intent",

    router,

    {

        "order":"order",

        "price":"price",

        "human":"human",

        "chat":"chat"

    }

)


workflow.add_edge(
    "order",
    END
)


workflow.add_edge(
    "price",
    END
)


workflow.add_edge(
    "human",
    END
)


workflow.add_edge(
    "chat",
    END
)



agent_graph=workflow.compile()
