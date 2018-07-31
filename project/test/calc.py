#첫 번째 숫자  입력 받으세요.
#두 번째 숫자  입력 받으세요.
#연산자 + - * / 입력 받으세요.

number1 = input("첫 번째 숫자  입력 해주세요.")
number2 = input("두 번째 숫자  입력 해주세요.")
operator = input("연산자 + - * / 입력 해주세요.")

number1 = int(number1)
number2 = int(number2)

if operator == "+":
    number3 = number1 + number2
elif operator == "-":
    number3 = number1 - number2
elif operator == "*":
    number3 = number1 * number2
elif operator == "/":
    number3 = number1 / number2

#들여쓰기는 문법

print(number1, operator, number2, "=", number3)


