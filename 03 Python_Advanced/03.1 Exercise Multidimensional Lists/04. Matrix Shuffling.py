def filling_the_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append([el for el in input().split(" ")])
        # matrix.append(list(map(str, input().split(" "))))
    return matrix
rows, cols = input().split()
matrix = filling_the_matrix(int(rows))
# print(matrix)

def swap(command, matrix):
    command = command.split(" ")
    if command[0] == "swap" and len(command) == 5:
        row_1, col_1 = int(command[1]), int(command[2])
        row_2, col_2 = int(command[3]), int(command[4])
        if (0 <= row_1 < len(matrix) and 0 <= col_1 < len(matrix[row_1]))\
                and (0 <= row_2 < len(matrix) and 0 <= col_2 < len(matrix[row_2])):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            for r in range(len(matrix)):
                print(*matrix[r], sep=" ")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    return matrix

command = input()
while not command == "END":
    swap(command, matrix)
    command = input()