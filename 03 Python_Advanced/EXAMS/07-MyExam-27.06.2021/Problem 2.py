matrix = [[b for b in input().split()] for x in range(5)]

my_position = []
for row in range(len(matrix)):
    if my_position:
        break
    for col in range(len(matrix)):
        if matrix[row][col] == "A":
            my_position.append(row), my_position.append(col)
            break


target_count = 0
for p in range(len(matrix)):
    for i in range(len(matrix)):
        if matrix[p][i] == "x":
            target_count += 1

num = int(input())
shooted_targets = 0
lst_hitted = []
for x in range(num):
    command = input().split()

    if command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        if direction == "right":
            if 0 <= my_position[1]+steps < len(matrix):
                if not matrix[my_position[0]][my_position[1]+steps] == "x":
                    matrix[my_position[0]][my_position[1]+steps] = "A"
                    matrix[my_position[0]][my_position[1]] = "."
                    my_position[1] += steps
        elif direction == "left":
            if 0 <= my_position[1] - steps < len(matrix):
                if not matrix[my_position[0]][my_position[1] - steps] == "x":
                    matrix[my_position[0]][my_position[1] - steps] = "A"
                    matrix[my_position[0]][my_position[1]] = "."
                    my_position[1] -= steps
        elif direction == "down":
            if 0 <= my_position[0] + steps < len(matrix):
                if not matrix[my_position[0]+steps][my_position[1]] == "x":
                    matrix[my_position[0]+steps][my_position[1]] = "A"
                    matrix[my_position[0]][my_position[1]] = "."
                    my_position[0] += steps
        elif direction == "up":
            if 0 <= my_position[0] - steps < len(matrix):
                if not matrix[my_position[0] - steps][my_position[1]] == "x":
                    matrix[my_position[0] - steps][my_position[1]] = "A"
                    matrix[my_position[0]][my_position[1]] = "."
                    my_position[0] -= steps

    elif command[0] == "shoot":
        direction = command[1]
        r = my_position[0]
        colll = my_position[1]
        if direction == "right":
            for a in range(colll+1, len(matrix)):
                if matrix[r][a] == "x":
                    matrix[r][a] = "."
                    lst_hitted.append([r, a])
                    shooted_targets += 1
                    break
        elif direction == "left":
            for b in range(colll, -1, -1):  # left
                if matrix[r][b] == "x":
                    matrix[r][b] = "."
                    lst_hitted.append([r, b])
                    shooted_targets += 1
                    break
        elif direction == "down":
            for c in range(r + 1, len(matrix)):  # down
                if matrix[c][colll] == "x":
                    matrix[c][colll] = "."
                    lst_hitted.append([c, colll])
                    shooted_targets += 1
                    break
        elif direction == "up":
            for d in range(r, -1, -1):  # Up
                if matrix[d][colll] == "x":
                    matrix[d][colll] = "."
                    lst_hitted.append([d, colll])
                    shooted_targets += 1

                    break

        if target_count - shooted_targets == 0:
            break
if target_count - shooted_targets == 0:
    print(f"Training completed! All {target_count} targets hit.")
elif target_count - shooted_targets > 0:
    print(f"Training not completed! {target_count - shooted_targets} targets left.")
for t in lst_hitted:
    print(t)