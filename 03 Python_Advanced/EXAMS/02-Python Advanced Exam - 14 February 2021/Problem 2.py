def filling_the_field(n):
    return [[el for el in input().split()] for _ in range(n)]


def finding_start_indices(field):
    return [[list_index, value_index] for list_index in range(len(field))
            for value_index in range(len(field[list_index]))
            if field[list_index][value_index] == "P"][0]


n = int(input())
field = filling_the_field(n)


current_position = finding_start_indices(field)
lost = False
coins = 0
directions = []

the_road = []

while coins <= 100:
    command = input()
    if command == "right":
        if (0 <= current_position[0] < len(field)) and (0 <= current_position[1]+1 < len(field)):
            if field[current_position[0]][current_position[1]+1].isdigit():
                coins += int(field[current_position[0]][current_position[1]+1])
                current_position = [current_position[0], current_position[1]+1]
                the_road.append(current_position)
            elif field[current_position[0]][current_position[1]+1] == "X":
                lost = True
                coins //= 2
                break
        else:
            lost = True
            coins //= 2
            break
    elif command == "left":
        if (0 <= current_position[0] < len(field)) and (0 <= current_position[1] - 1 < len(field)):
            if field[current_position[0]][current_position[1] - 1].isdigit():
                coins += int(field[current_position[0]][current_position[1] - 1])
                current_position = [current_position[0], current_position[1] - 1]
                the_road.append(current_position)
            elif field[current_position[0]][current_position[1] - 1] == "X":
                lost = True
                coins //= 2
                break
        else:
            lost = True
            coins //= 2
            break
    elif command == "up":
        if (0 <= current_position[0]-1 < len(field)) and (0 <= current_position[1] < len(field)):
            if field[current_position[0]-1][current_position[1]].isdigit():
                coins += int(field[current_position[0]-1][current_position[1]])
                current_position = [current_position[0]-1, current_position[1]]
                the_road.append(current_position)
            elif field[current_position[0]-1][current_position[1]] == "X":
                lost = True
                coins //= 2
                break
        else:
            lost = True
            coins //= 2
            break
    elif command == "down":
        if (0 <= current_position[0] + 1 < len(field)) and (0 <= current_position[1] < len(field)):
            if field[current_position[0] + 1][current_position[1]].isdigit():
                coins += int(field[current_position[0] + 1][current_position[1]])
                current_position = [current_position[0] + 1, current_position[1]]
                the_road.append(current_position)
            elif field[current_position[0] + 1][current_position[1]] == "X":
                lost = True
                coins //= 2
                break
        else:
            lost = True
            coins //= 2
            break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
    print(f"Your path:")
    for d in the_road:
        print(d)
elif lost:
    print(f"Game over! You've collected {coins} coins.")
    print(f"Your path:")
    for d in the_road:
        print(d)