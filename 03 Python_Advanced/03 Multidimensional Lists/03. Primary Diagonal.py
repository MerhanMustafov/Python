def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(read_int_list_from_input())

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)


# def matrix_read():
#     size = int(input())
#     matrix = []
#     for row_index in range(size):
#         row = list(map(int, input().split(" ")))
#         matrix.append(row)
#     return matrix
#
# def get_primary_diagonal_sum(matrix):
#     diagonal_sum = 0
#     for i in range(len(matrix)):
#         diagonal_sum += matrix[i][i]
#     return diagonal_sum
#
# def get_sum_below_primary_diagonal(matrix):
#     the_sum = 0
#     size = len(matrix)
#     for r in range(size):
#         for c in range(size):
#             if c <= r:
#                 the_sum += matrix[r][c]
#
#     return the_sum
# print(get_primary_diagonal_sum(matrix_read()))
# print(get_sum_below_primary_diagonal(matrix_read()))
#
#
