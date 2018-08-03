from random import *
"""
숙제
- 게임판의 크기를 지정하도록 변경
- 게임판의 크기에 따라 지뢰의 갯수 변경
- 지뢰 표시 기능 추가
- 지뢰의 위치를 저장한 리스트를 따로 사용하고 매트릭스는 하나만 사용하도록 수정

"""
import sys
import time

matrix_i_length, matrix_j_length = input("게임판의 크기를 입력하여 주세요. > ").split()
matrix_i_length, matrix_j_length = int(matrix_i_length), int(matrix_j_length)

mine = matrix_j_length

result_matrix = []
# 게임칸의 크기 설정
for i in range(matrix_i_length):
    result_matrix_add=[]
    for j in range(matrix_j_length):
        result_matrix_add.append('+')
    result_matrix.append(result_matrix_add)

mine_matrix = []
# 행마다 지뢰 1개씩 추가
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
    row = [row_index - 1, row_index, row_index + 1]
    column = [column_index - 1, column_index, column_index + 1]

    mine_count = 0

    for i in row:
        for j in column:
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
    for i in range(matrix_i_length):
        for j in range(matrix_j_length):
            print("{0:>2}".format(result_matrix[i][j]), end="")
        print()

# 정답 공개
def x_matrix():
    for i in range(matrix_i_length):
        for j in range(matrix_j_length):
            print("{0:>2}".format(mine_matrix[i][j]), end="")
        print()


# 입력값이 Q이면 게임을 멈추는 메서드
def end_game(user_input):
    if 'Q' == user_input.upper():
        print("게임을 그만합니다.")
        sys.exit(0)

def get_row_and_column(index):
    index = index - 1
    row = index // matrix_i_length
    column = index % matrix_i_length
    return row, column


def found_mine_counter():
    plus_count = 0
    for i in range(matrix_i_length):
        for j in range(matrix_j_length):
            if mine_matrix[i][j] == '*' and result_matrix[i][j] == 'X':
                plus_count +=1

    return plus_count == mine

def main():
    # 현재 시간을 측정하여 값 넣어줌
    start_time = time.time()

    while True:
        view_matrix()
        user_input, why = input('> ').split()
        end_game(user_input)

        # print("user_input :", user_input)
        i, j = get_row_and_column(int(user_input))

        if why == "!":
            # print('i', i, 'j', j)
            mine_count = mine_counter(i, j)
            result_matrix[i][j] = mine_count
        elif why == "?":
            mine_count = ''
            result_matrix[i][j] = "X"

        if mine_count == '*':
            x_matrix()
            print("지뢰를 밟았습니다!")
            end_time = time.time()
            print(int(end_time - start_time), "초 경과")
            sys.exit(0)

        if found_mine_counter():
            x_matrix()
            print("모든 지뢰를 찾았습니다.")
            end_time = time.time()
            print(int(end_time - start_time), "초 경과")
            sys.exit(0)



if __name__ == '__main__':
    main()
print('__main__')