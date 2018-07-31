from random import *

print("게임을 시작하겠습니다.")
order = [("청기 올려", "R"),
         ("청기 내려", "F"),
         ("청기 내리지말고 올려", "R"),
         ("청기 올리지말고 내려", "F"),
         ("백기 올려", "U"),
         ("백기 내려", "J"),
         ("백기 내리지말고 올려", "U"),
         ("백기 올리지말고 내려", "J")]

cnt = 0

while True:
    random_index = randrange(len(order))
    message, button = order[random_index]

    print("> ", message)
    user_input = input("> ")

    if button == user_input.upper():
        print("성공")
        cnt +=1
    elif user_input.upper()=="Q":
        print("게임을 종료하겠습니다.")
        print(cnt, "번 성공하였습니다.")
        break
    else:
        print("실패")
        print(cnt, "번 성공하였습니다.")
        break