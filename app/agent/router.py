def router(state):


    intent = state["intent"]


    if intent=="order":

        return "order"


    elif intent=="price":

        return "price"


    elif intent=="human":

        return "human"


    else:

        return "chat"