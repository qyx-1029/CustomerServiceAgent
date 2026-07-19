def query_price(product:str):


    prices={

        "机器人":
        "价格2999元",

        "沙发":
        "价格5999元"

    }


    return prices.get(

        product,

        "暂无价格信息"

    )