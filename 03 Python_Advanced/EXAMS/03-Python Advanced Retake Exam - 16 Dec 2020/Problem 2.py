def read_matrix(n):
    return [[x for x in input()] for el in range(n)]

def initial_position(field):
    pos = []
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "P":
                pos.append(r), pos.append(c)
    return pos


initial_string = input()
n = int(input())
field = read_matrix(n)

cur_pos = initial_position(field)
m = int(input())
while m > 0:
    command = input()
    if command == "right":
        if (0 <= cur_pos[0] < len(field)) and (0 <= cur_pos[1] + 1 < len(field)):
            if  field[cur_pos[0]][cur_pos[1] +1].isalpha():
                initial_string += field[cur_pos[0]][cur_pos[1]+1]
                field[cur_pos[0]][cur_pos[1]] = "-"
                field[cur_pos[0]][cur_pos[1]+1] = "P"
                cur_pos[1] += 1
            else:

                field[cur_pos[0]][cur_pos[1]] = "-"
                field[cur_pos[0]][cur_pos[1] + 1] = "P"
                cur_pos[1] += 1
        else:
            if initial_string:
                initial_string = initial_string[0:-1]
    elif command == "left":
        if (0 <= cur_pos[0] < len(field)) and (0 <= cur_pos[1] -1 < len(field)):
            if  field[cur_pos[0]][cur_pos[1] -1].isalpha():
                initial_string += field[cur_pos[0]][cur_pos[1] - 1]
                field[cur_pos[0]][cur_pos[1]] = "-"
                field[cur_pos[0]][cur_pos[1] - 1] = "P"
                cur_pos[1] -= 1
            else:

                field[cur_pos[0]][cur_pos[1]] = "-"
                field[cur_pos[0]][cur_pos[1] - 1] = "P"
                cur_pos[1] -= 1
        else:
            if initial_string:
                initial_string = initial_string[0:-1]
    elif command == "up":
        if (0 <= cur_pos[0]-1 < len(field)) and (0 <= cur_pos[1] < len(field)):
            if  field[cur_pos[0]-1][cur_pos[1]].isalpha():
                initial_string += field[cur_pos[0]-1][cur_pos[1]]
                field[cur_pos[0]][cur_pos[1]] = "-"
                field[cur_pos[0] - 1][cur_pos[1]] = "P"
                cur_pos[0] -= 1
            else:

                field[cur_pos[0]][cur_pos[1]] = "-"
                field[cur_pos[0] - 1][cur_pos[1]] = "P"
                cur_pos[0] -= 1
        else:
            if initial_string:
                initial_string = initial_string[0:-1]
    elif command == "down":
        if (0 <= cur_pos[0]+1 < len(field)) and (0 <= cur_pos[1] < len(field)):
            if  field[cur_pos[0]+1][cur_pos[1]].isalpha():
                initial_string += field[cur_pos[0]+1][cur_pos[1]]
                field[cur_pos[0]][cur_pos[1]] = "-"
                field[cur_pos[0] + 1][cur_pos[1]] = "P"
                cur_pos[0] += 1
            else:

                field[cur_pos[0]][cur_pos[1]] = "-"
                field[cur_pos[0] + 1][cur_pos[1]] = "P"
                cur_pos[0] += 1
        else:
            if initial_string:
                initial_string = initial_string[0:-1]


    m -= 1
print(initial_string)
for el in field:
    print(*el, sep="")