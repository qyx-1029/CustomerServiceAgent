def query_order(order_id:str):

    """
    查询订单状态
    """

    # 模拟数据库

    orders={

        "123456":
        {
            "status":"已发货",
            "delivery":"明天送达"
        }

    }


    order=orders.get(order_id)


    if order:

        return (
            f"订单状态:{order['status']},"
            f"预计:{order['delivery']}"
        )


    return "没有找到该订单"