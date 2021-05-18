def filling_the_matrix(rows):
    matrix = []
    for row in range(rows):
        matrix.append(list(map(str, input().split(" "))))
    return matrix


def count_squares(matrix):
    count = 0
    for row in range(len(matrix) - 1):
        for col in range(len(matrix[row]) - 1):
            if (matrix[row][col] == matrix[row][col + 1]) and (matrix[row][col] == matrix[row + 1][col]) and matrix[row][col] == matrix[row + 1][col + 1]:

            # if (matrix[row][col] == matrix[row + 1][col]) and (matrix[row][col + 1] == matrix[row + 1][col + 1]):
                count += 1
    return count


rows, cols = input().split(" ")
matrix = filling_the_matrix(int(rows))
result = count_squares(matrix)
print(result)
