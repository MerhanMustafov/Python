matrix = [input().split() for index in range(int(input()))]

def recursion(start_r, count_, matrix_):
    is_bad = False
    for row in range(start_r, len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '1':
                if row in range(len(matrix) - 1) and col in range(len(matrix[row]) - 1) and matrix[row][col+1] == '1' \
                        and matrix[row + 1][col] == '1':
                    is_bad = True
                if row in range(len(matrix) - 1) and matrix[row+1][col] == '1':
                    matrix[row][col] = 0
                elif col in range(len(matrix[row]) - 1) and matrix[row][col+1] == '1':
                    matrix[row][col] = 0
                else:
                    if is_bad:
                        pass
                    else:
                        if row in range(len(matrix) - 1) and matrix[row-1][col] == '1':
                            pass
                        else:
                            count_ += 1
        is_bad = False
        start_r += 1
        return recursion(start_r, count_, matrix_)
    return count_


print(recursion(0, 0, matrix))