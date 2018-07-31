from random import *

number = randrange(0,10)

cnt = int(1)
guess_number = int(input("값을 입력하여 주세요.>"))
while True:

    if number == guess_number:
        print("정답입니다. 시도하신 횟수는", cnt, "번 입니다.")
        break
    else:
        cnt +=1
        if number > guess_number:
            guess_number = int(input("더 큰 숫자를 입력하여 주세요.>"))
        elif number < guess_number:
            guess_number = int(input("더 작은 숫자를 입력하여 주세요.>"))
        continue
