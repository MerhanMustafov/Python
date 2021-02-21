rows = int(input())
maze = [input() for row in range(rows)]

moves = 0
kat_pos = 0
for row in range(len(maze)):
    for one in range(len(maze[row])):
        if maze[one] == " ":
            moves += 1
            continue
        else:
            moves = 0
        if maze[one] == "k":
            kat_pos = row
            if moves > 0:
                print(f"Kate got out in {moves} moves")
                exit(0)
            else:
                continue

