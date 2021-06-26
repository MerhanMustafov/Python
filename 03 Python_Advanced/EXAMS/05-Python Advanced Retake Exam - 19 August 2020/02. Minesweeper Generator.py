def read_matrix(size):
    return [[None]*size for _ in range(size)]

def bomb_positions(num_bombs):
    bomb_coordinates = []
    for position in range(num_bombs):
        data = input()
        row, col = [int(n) for n in data[1:-1].split(", ")]
        # if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        bomb_coordinates.append([row, col])
    return bomb_coordinates

def placing_the_bombs(matrix, bomb_pos):
    for pos in bomb_pos:
        matrix[pos[0]][pos[1]] = "*"
    return matrix


size = int(input())
matrix = read_matrix(size)

num_bombs = int(input())
bomb_pos = bomb_positions(num_bombs)

matrix = placing_the_bombs(matrix, bomb_pos)

count = 0
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "*":
            continue
        if row == 0:
            if col == 0:
                if matrix[row][col+1] == "*":#right
                    count += 1
                if matrix[row+1][col] == "*":#down
                    count += 1
                if matrix[row+1][col+1] == "*":#downright
                    count += 1
            elif col == len(matrix)-1:
                if matrix[row][col-1] == "*":#left
                    count += 1
                if matrix[row+1][col] == "*":#down
                    count += 1
                if matrix[row+1][col-1] == "*":#downleft
                    count += 1
            else:
                if matrix[row][col+1] == "*":#right
                    count += 1
                if matrix[row][col-1] == "*":#left
                    count += 1
                if matrix[row+1][col] == "*":#down
                    count += 1
                if matrix[row+1][col+1] == "*":#downright
                    count += 1
                if matrix[row+1][col-1] == "*":#downleft
                    count += 1


        elif row == len(matrix) - 1:
            if col == 0:
                if matrix[row][col+1] == "*":#right
                    count += 1
                if matrix[row-1][col] == "*":#up
                    count += 1
                if matrix[row-1][col+1] == "*":#upright
                    count += 1
            elif col == len(matrix) - 1:
                if matrix[row][col - 1] == "*":#left
                    count += 1
                if matrix[row - 1][col] == "*":#up
                    count += 1
                if matrix[row - 1][col - 1] == "*":#upleft
                    count += 1
            else:
                if matrix[row][col+1] == "*":#right
                    count += 1
                if matrix[row][col-1] == "*":#left
                    count += 1
                if matrix[row-1][col] == "*":#up
                    count += 1
                if matrix[row-1][col+1] == "*":#upright
                    count += 1
                if matrix[row-1][col-1] == "*":#upleft
                    count += 1

        else:
            if col == 0:
                if matrix[row][col+1] == "*": #right
                    count += 1
                if matrix[row+1][col] == "*":#down
                    count += 1
                if matrix[row-1][col] == "*":#up
                    count += 1
                if matrix[row-1][col+1] == "*":#upright
                    count += 1
                if matrix[row+1][col+1] == "*":#downright
                    count += 1
            elif col == len(matrix) - 1:
                if matrix[row][col-1] == "*": #left
                    count += 1
                if matrix[row+1][col] == "*":#down
                    count += 1
                if matrix[row-1][col] == "*":#up
                    count += 1
                if matrix[row-1][col-1] == "*":#upleft
                    count += 1
                if matrix[row+1][col-1] == "*":#downleft
                    count += 1
            else:
                if matrix[row][col+1] == "*": #right
                    count += 1
                if matrix[row][col-1] == "*": #left
                    count += 1
                if matrix[row+1][col] == "*":#down
                    count += 1
                if matrix[row-1][col] == "*":#up
                    count += 1
                if matrix[row-1][col+1] == "*":#upright
                    count += 1
                if matrix[row+1][col+1] == "*":#downright
                    count += 1
                if matrix[row-1][col-1] == "*":#upleft
                    count += 1
                if matrix[row+1][col-1] == "*":#downleft
                    count += 1

        matrix[row][col] = count
        count = 0
for r in matrix:
    print(*r,sep=" ")