def read_matrix(n):
    return [[int(row) for row in input().split()]for _ in range(n)]

n = int(input())
matrix = read_matrix(n)
# print(matrix)

command = input()
while not command == "END":
    typee, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if typee == "Add":
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    command = input()

# for row in matrix:
#     print(*row, sep=" ")

[print(*row, sep=" ") for row in matrix]