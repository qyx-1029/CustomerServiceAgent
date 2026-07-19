from app.memory.memory_manager import *


save_message(

"user001",

"user",

"我要查订单"

)



save_message(

"user001",

"assistant",

"请输入订单号"

)



print(
    get_history("user001")
)
