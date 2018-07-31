from random import *

print("게임을 시작하겠습니다.")
order = {"청기 올려":"R", "청기 내려":"F", "백기 올려":"U", "백기 내려":"J"}
#dictionary 앞에값이 key값이고 뒤에가 value값 / key값을 넣으면 value값을 가져올 수 있음
#value=order["청기 올려"]

order_messages = list(order.keys())
while True:
    random_index = randrange(len(order_messages))
    message = order_messages[random_index]

    print("> ", message)
    button = order[message]

    user_input = input("> ")

    if button == user_input.upper():
        print("성공")
    else:
        print("실패")