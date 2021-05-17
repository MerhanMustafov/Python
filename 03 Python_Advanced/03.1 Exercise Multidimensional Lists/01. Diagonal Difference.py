def creating_the_matrix(square):
    matrix = []
    for row in range(square):
        matrix.append(list(map(int, input().split(" "))))
    return matrix

def sum_first_diagonal(matrix):
    sum = 0
    for row_index in range(len(matrix)):
        row = matrix[row_index]
        count = row_index
        sum += row[count]
    return sum

def sum_second_diagonal(matrix):
    sum = 0
    count = -1
    for row_index in range(len(matrix)):
        row = matrix[row_index]
        sum += row[count]
        count += -1
    return sum

def print_result(first_diag, sec_diag):
    return abs(first_diag - sec_diag)


square = int(input())
matrix = creating_the_matrix(square)
# print(matrix)
first_diagonal_sum = sum_first_diagonal(matrix)
# print(first_diagonal_sum)
second_diagonal_sum = sum_second_diagonal(matrix)
# print(second_diagonal_sum)
result = print_result(first_diagonal_sum, second_diagonal_sum)
print(result)