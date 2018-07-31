"""
마인매트릭스를 전체를 돌면서 주변의 지뢰갯수를 설정
"""
mine_matrix = [['-', '-', '-', '*', '-'],
               ['-', '*', '-', '-', '-'],
               ['-', '-', '-', '-', '*'],
               ['-', '*', '-', '-', '-'],
               ['-', '-', '*', '-', '-']]

matrix_i_length = len(mine_matrix)
matrix_j_length = len(mine_matrix[0])


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

            if 0 <= i < matrix_i_length and 0 <= j < matrix_j_length:
                # print("(", i, j, ")", end=", ")
                # print(matrix[i][j], end="")
                if mine_matrix[i][j] == '*':
                    mine_count = mine_count + 1
        # print()
    return mine_count


# 지뢰 출력
print("설정전")
for i in range(matrix_i_length):
    for j in range(matrix_j_length):
        print("{0:>2}".format(mine_matrix[i][j]), end="")
    print()





# 지뢰 갯수 찾아서 설정
for i in range(matrix_i_length):
    for j in range(matrix_j_length):
        mine_matrix[i][j] = mine_counter(i, j)

while True:
    i, j = input("값을 입력해주세요").split(",")
    mine_counter(int(i),int(j))
    break

# # 지뢰 출력
# print("\n설정 후")
# for i in range(matrix_i_length):
#     for j in range(matrix_j_length):
#         print("{0:>2}".format(mine_matrix[i][j]), end="")
#     print()

