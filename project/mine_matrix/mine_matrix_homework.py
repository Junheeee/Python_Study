from random import *
"""
숙제
- 게임판의 크기를 지정하도록 변경 o
- 게임판의 크기에 따라 지뢰의 갯수 변경 o
- 지뢰 표시 기능 추가
- 지뢰의 위치를 저장한 리스트를 따로 사용하고 매트릭스는 하나만 사용하도록 수정 o

"""
import sys
import time

#게임칸의 크기를 지정하는 값 입력받기
matrix_i_length, matrix_j_length = input().split()
matrix_i_length, matrix_j_length = int(matrix_i_length), int(matrix_j_length)

#지뢰의 갯수(열의 크기만큼)
mine = matrix_j_length

result_matrix = []
#게임칸의 크기 설정
for i in range(matrix_i_length):
    result_matrix_add=[]
    for j in range(matrix_j_length):
        result_matrix_add.append('+')
    result_matrix.append(result_matrix_add)

mine_matrix = []
#행마다 지뢰 1개씩 추가
for i in range(matrix_i_length):
        mine_matrix_add=[]
        random = randrange(matrix_j_length)+1
        for j in range(matrix_j_length):
            if j == random-1:
                mine_matrix_add.append('*')
            else:
                mine_matrix_add.append('.')
        mine_matrix.append(mine_matrix_add)

def mine_counter(row_index, column_index):
    """
    주변 9칸의 지뢰 갯수를 찾는 함수

    row_index = 2
    column_index = 2
    라고 가정했을 때 확인해야할 인덱스들

    (-1, -1) (-1, -) (-1, +1)
     (-, -1)  (2, 2)  (-, +1)
    (+1, -1) (+1, -) (+1, +1)

    """

    # 확인하려는 인덱스의 값이 지뢰일때는 바로 반환
    if mine_matrix[row_index][column_index] == '*':
        return '*'

    # 확인할 인덱스 생성
    #예시(0,2) 3번
    #row_index = 0
    #column_index = 2
    #row = [-1,0,1]
    #column = [1,2,3]
    row = [row_index - 1, row_index, row_index + 1]
    column = [column_index - 1, column_index, column_index + 1]

    mine_count = 0

    for i in row:
        for j in column:
            #0==-1 and 2==+1 -> 실행x
            #0== 0 and 2==+2 -> 해당 for문 실행안하고 다음for문으로 넘기기
            #0==+1 and 2==+3 -> 실행x
            if row_index == row and column_index == column:
                continue

            #
            if 0 <= i < matrix_i_length and 0 <= j < matrix_j_length:
                # print("(", i, j, ")", end=", ")
                # print(matrix[i][j], end="")
                if mine_matrix[i][j] == '*':
                    mine_count = mine_count + 1
                else:
                    result_matrix[i][j] = '.'
        # print()
    return mine_count


# 지뢰 출력
def view_matrix():
    for i in range(matrix_i_length): #0~4
        for j in range(matrix_j_length): #0~4
            #result_matrix[i][j]의 값(+)을 화살표 방향대로 두칸띄어놓고(출력값포함) 출력하라
            #{0}의 예시 : print("{0}".format(5)) // 5
            print("{0:>2}".format(result_matrix[i][j]), end="") #줄바꿈 X
        print()


# 입력값이 Q이면 게임을 멈추는 메서드
def end_game(user_input):
    if 'Q' == user_input.upper():
        print("게임을 그만합니다.")
        sys.exit(0)


#index = 입력값
#입력값의 좌표를 구하는 메서드
def get_row_and_column(index):
    index = index - 1
    #// - 나눠서 소숫점 아래자리를 버리고 반환
    #row = 입력값 // 5
    row = index // matrix_i_length
    #% - 나눠서 나머지 반환
    #column = 입력값 % 5
    column = index % matrix_i_length
    return row, column


def found_mine_counter():
    plus_count = 0

    for i in range(matrix_i_length): #5
        for j in range(matrix_j_length): #5
            if result_matrix[i][j] == '+':
                plus_count = plus_count + 1

    return plus_count == mine

def main():
    #현재 시간을 측정하여 값 넣어줌
    start_time = time.time()

    while True:
        #지뢰를 출력하는 view_matrix()실행
        view_matrix()

        #입력값을 user_input에 넣어줌
        user_input = input('> ')

        #입력값을 인자로 받는 end_game() 실행
        #입력값이 Q인경우 게임 종료
        end_game(user_input)

        # print("user_input :", user_input)
        #입력값을 인자로 받는 get_row_and_column()실행하여 출력값을 i, j에 넣어줌
        #입력값의 좌표를 구하는 메서드
        i, j = get_row_and_column(int(user_input))
        # print('i', i, 'j', j)
        #i, j를 인자로 받고, 주변 지뢰 갯수를 찾는 mine_counter() 실행
        #입력값의 위치가 지뢰인 경우 mine_count에 *이 들어감
        mine_count = mine_counter(i, j)
        #입력값의 좌표에
        result_matrix[i][j] = mine_count

        if mine_count == '*':
            # 지뢰를 출력하는 view_matrix()실행
            view_matrix()
            print("지뢰를 밟았습니다!")
            #게임 끝난 시간을 측정하여 값 넣어줌
            end_time = time.time()
            #끝난시간에서 시작한 시간을 넣어 경과시간을 구함
            print(int(end_time - start_time), "초 경과")
            #게임 종료
            sys.exit(0)

        if found_mine_counter():
            # 지뢰를 출력하는 view_matrix()실행
            view_matrix()
            print("모든 지뢰를 찾았습니다.")
            # 게임 끝난 시간을 측정하여 값 넣어줌
            end_time = time.time()
            # 끝난시간에서 시작한 시간을 넣어 경과시간을 구함
            print(int(end_time - start_time), "초 경과")
            #게임 종료
            sys.exit(0)

#matrix라는 모듈입장에서는 이 모듈이 main이기 때문에 if문이 동작됨
if __name__ == '__main__':
    main()
