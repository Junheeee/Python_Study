print("> 수비수가 고른 숫자")
number1 = 3
number2 = 2
number3 = 0
print(number1)
print(number2)
print(number3)

print("첫번째 숫자를 입력하세요.")
guess_number1 = int(input("prompt>"))
print("두번째 숫자를 입력하세요.")
guess_number2 = int(input("prompt>"))
print("세번째 숫자를 입력하세요.")
guess_number3 = int(input("prompt>"))

print("> 공격수가 고른 숫자")
print(guess_number1)
print(guess_number2)
print(guess_number3)

if(guess_number1 == guess_number2)or(guess_number2 == guess_number3)or(guess_number3 == guess_number1):
    print("겹치는 숫자가 있습니다.")
else:
    strike_count = 0
    ball_count= 0

if(number1 == guess_number1):
    strike_count +=1
elif(number1 == guess_number2):
    ball_count +=1
elif(number1 == guess_number3):
    ball_count+=1

if(number2 == guess_number2):
    strike_count +=1
elif(number2 == guess_number1):
    ball_count +=1
elif(number2 == guess_number3):
    ball_count+=1

if(number3 == guess_number3):
    strike_count +=1
elif(number3 == guess_number2):
    ball_count +=1
elif(number3 == guess_number1):
    ball_count+=1


print("스트라이크 : ", strike_count)
print("볼 : ", ball_count)
print("아웃 : ", 3 - strike_count - ball_count)