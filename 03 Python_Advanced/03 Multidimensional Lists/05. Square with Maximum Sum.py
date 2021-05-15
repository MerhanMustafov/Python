def matrix_read():
    (rows_count, columns_count) = map(int, input().split(", "))
    matrix = []
    for row_index in range(rows_count):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix
def get_sum_of_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum

#
# matrix = matrix_read()
def get_best_submatrix_sum_corrdinated(matrix, submatrix_size):


    best_row_index = 0
    best_column_index = 0
    best_sum = get_sum_of_submatrix(matrix, 0, 0, submatrix_size)

    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sums = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
            if best_sum < current_sums:
                best_sum = current_sums
                best_row_index = row_index
                best_column_index = col_index
    return (best_row_index, best_column_index)
def print_result(coodinates, size):
    (row_index, col_index) = coodinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(get_sum_of_submatrix(matrix, row_index, col_index, SUBMATRIX_SIZE))

SUBMATRIX_SIZE = 2
matrix = matrix_read()
coordinates = get_best_submatrix_sum_corrdinated(matrix, SUBMATRIX_SIZE)
print_result(coordinates, SUBMATRIX_SIZE)


