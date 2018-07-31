from random import *

print("+----------------------------------------------------------+")
print("|                      숫자 야구 게임                      |")
print("+----------------------------------------------------------+")
print("| 수비수가 고른 세자릿수를 맞춰보세요.                     |")
print("| 0에서 9까지 서로 다른 숫자이다. (같은 숫자 사용 금지)    |")
print("| 스트라이크 : 공격수가 제시한 숫자와 위치가 모두 맞을 경우|")
print("| 볼 : 공격수가 제시한 숫자는 맞고 위치가 틀릴 경우        |")
print("| 아웃 : 공격수가 제시한 숫자가 모두 틀릴 경우             |")
print("+----------------------------------------------------------+")

base_ball_len = 3

ran_num = [] #list
inp_num = [] #list

index = 0

while index < base_ball_len:
    ran_num.append(randrange(0, 10))
    has_a = False

    for i in range(index):
        if ran_num[index] == ran_num[i]:
            has_a = True
            ran_num.pop()
            break

    if not has_a:
        index +=1

while True:
    inp_num.clear()
    for i in range(base_ball_len):
        a = i+1
        inp_num.append(int(input("> " + str(a) + "번째 숫자를 입력하세요")))

    ran_inp = {tuple(ran_num): inp_num}  # dic

    if inp_num[0]==inp_num[1] or inp_num[0]==inp_num[2] or inp_num[1]==inp_num[2]:
        print("같은 숫자를 입력하면 안 됩니다.")
        continue

    str_b = 0
    b = 0

    for j in range(base_ball_len):
        for i in range(base_ball_len):
            # if ran_inp[0][j]== ran_inp[1][i]:
            #     if j==i:
            #         str_b +=1
            #     else:
            #         b+=1
            if ran_num[j] == inp_num[i]:
                if j == i:
                    str_b +=1
                else:
                    b +=1

    print("스트라이크 :", str_b)
    print("볼 :", b)
    print("아웃 :", base_ball_len-str_b-b)

    if str_b ==3:
        print("정답! 게임 끝")
        break