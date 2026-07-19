from app.prompts.customer_service import (
    CUSTOMER_SERVICE_SYSTEM_PROMPT
)

from app.prompts.order import (
    ORDER_PROMPT
)

from app.prompts.after_sale import (
    AFTER_SALE_PROMPT
)

from app.prompts.sales import (
    SALES_PROMPT
)


# 新版Prompt管理

def get_prompt(scene="customer_service"):


    prompts = {

        "customer_service":
            CUSTOMER_SERVICE_SYSTEM_PROMPT,

        "order":
            ORDER_PROMPT,

        "after_sale":
            AFTER_SALE_PROMPT,

        "sales":
            SALES_PROMPT

    }


    return prompts.get(
        scene,
        CUSTOMER_SERVICE_SYSTEM_PROMPT
    )


# 兼容旧代码
# llm_service.py 目前还在使用它

def get_customer_service_prompt():

    return get_prompt(
        "customer_service"
    )