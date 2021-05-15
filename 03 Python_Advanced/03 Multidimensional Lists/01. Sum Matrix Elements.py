
def matrix_read():
    (row_count, column_count) = list(map(int, input().split(", ")))
    matrix = []
    for row_index in range(row_count):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix

matrix = matrix_read()
matrix_sum = 0

for r in range(len(matrix)):
    row = matrix[r]
    for c in range(len(row)):
        matrix_sum += row[c]
print(matrix_sum)
print(matrix)