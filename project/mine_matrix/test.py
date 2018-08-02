from random import *
matrix_i_length, matrix_j_length = input().split()
matrix_i_length, matrix_j_length = int(matrix_i_length), int(matrix_j_length)

mine = matrix_j_length

result_matrix = []

for i in range(matrix_i_length):
    result_matrix_add=[]
    for j in range(matrix_j_length):
        result_matrix_add.append('+')
    result_matrix.append(result_matrix_add)

print(result_matrix)

mine_matrix = []

for i in range(matrix_i_length):
        mine_matrix_add=[]
        random = randrange(matrix_j_length)+1
        for j in range(matrix_j_length):
            if j == random-1:
                mine_matrix_add.append('*')
            else:
                mine_matrix_add.append('.')
        mine_matrix.append(mine_matrix_add)

print(mine_matrix)