
def read_teritory(n):
    return [[b for b in input()] for x in range(n)]

def snake_position(teritory):
    position = None
    for row in range(len(teritory)):
        for col in range(len(teritory)):
            if teritory[row][col] == "S":
                position = [row, col]
                break
        break
    return position

def check_if_burrows(teritory):
    for row in range(len(teritory)):
        for col in range(len(teritory)):
            if teritory[row][col] == "B":
                return True
    return False

def burrows_position(teritory):
    position = []
    for row in range(len(teritory)):
        for col in range(len(teritory)):
            if teritory[row][col] == "B":
                position.append([row, col])
    return position
n = int(input())
teritory = read_teritory(n)
snake_pos = snake_position(teritory)

if check_if_burrows(teritory):
    burrows_pos = burrows_position(teritory)


food_eaten = 0
game_over = False
while True:
    command = input()
    if command == "up":
        if 0 <= snake_pos[0] - 1 < n:
            if teritory[snake_pos[0] - 1][snake_pos[1]] == "B":
                teritory[snake_pos[0]][snake_pos[1]] = "."
                teritory[snake_pos[0] - 1][snake_pos[1]] = "."
                snake_pos[0] -= 1
                for a in range(len(burrows_pos)):
                    if burrows_pos[a] == snake_pos:
                        burrows_pos.pop(a)
                    else:
                        burrows_pos.pop(a + 1)
                    teritory[burrows_pos[0][0]][burrows_pos[0][1]] = "S"
                    snake_pos[0] = burrows_pos[0][0]
                    snake_pos[1] = burrows_pos[0][1]
                    burrows_pos.pop()
                    break
            else:
                if teritory[snake_pos[0]-1][snake_pos[1]] == "*":
                    food_eaten += 1
                teritory[snake_pos[0]][snake_pos[1]]  = "."
                teritory[snake_pos[0]-1][snake_pos[1]] = "S"
                snake_pos[0] -= 1
        else:
            game_over = True
            break
    elif command == "down":
        if 0 <= snake_pos[0] + 1 < n:
            if teritory[snake_pos[0] + 1][snake_pos[1]] == "B":
                teritory[snake_pos[0]][snake_pos[1]] = "."
                teritory[snake_pos[0] + 1][snake_pos[1]] = "."
                snake_pos[0] += 1
                for b in range(len(burrows_pos)):
                    if burrows_pos[b] == snake_pos:
                        burrows_pos.pop(b)
                    else:
                        burrows_pos.pop(b + 1)
                    teritory[burrows_pos[0][0]][burrows_pos[0][1]] = "S"
                    snake_pos[0] = burrows_pos[0][0]
                    snake_pos[1] = burrows_pos[0][1]
                    burrows_pos.pop()
                    break
            else:
                if teritory[snake_pos[0] + 1][snake_pos[1]] == "*":
                    food_eaten += 1
                teritory[snake_pos[0]][snake_pos[1]] = "."
                teritory[snake_pos[0] + 1][snake_pos[1]] = "S"
                snake_pos[0] += 1
        else:
            game_over = True
            break
    elif command == "left":
        if 0 <= snake_pos[1] - 1 < n:
            if teritory[snake_pos[0]][snake_pos[1] - 1] == "B":
                teritory[snake_pos[0]][snake_pos[1]] = "."
                teritory[snake_pos[0]][snake_pos[1] - 1] = "."
                snake_pos[1] -= 1
                for c in range(len(burrows_pos)):
                    if burrows_pos[c] == snake_pos:
                        burrows_pos.pop(c)
                    else:
                        burrows_pos.pop(c + 1)
                    teritory[burrows_pos[0][0]][burrows_pos[0][1]] = "S"
                    snake_pos[0] = burrows_pos[0][0]
                    snake_pos[1] = burrows_pos[0][1]
                    burrows_pos.pop()
                    break
            else:
                if teritory[snake_pos[0]][snake_pos[1] - 1] == "*":
                    food_eaten += 1
                teritory[snake_pos[0]][snake_pos[1]] = "."
                teritory[snake_pos[0]][snake_pos[1] - 1] = "S"
                snake_pos[1] -= 1
        else:
            game_over = True
            break
    elif command == "right":
        if 0 <= snake_pos[1] + 1 < n:
            if teritory[snake_pos[0]][snake_pos[1] + 1] == "B":
                teritory[snake_pos[0]][snake_pos[1]] = "."
                teritory[snake_pos[0]][snake_pos[1] + 1] = "."
                snake_pos[1] += 1
                for d in range(len(burrows_pos)):
                    if burrows_pos[d] == snake_pos:
                        burrows_pos.pop(d)
                    else:
                        burrows_pos.pop(d + 1)
                    teritory[burrows_pos[0][0]][burrows_pos[0][1]] = "S"
                    snake_pos[0] = burrows_pos[0][0]
                    snake_pos[1] = burrows_pos[0][1]
                    burrows_pos.pop()
                    break
            else:
                if teritory[snake_pos[0]][snake_pos[1] + 1] == "*":
                    food_eaten += 1
                teritory[snake_pos[0]][snake_pos[1]]  = "."
                teritory[snake_pos[0]][snake_pos[1] + 1] = "S"
                snake_pos[1] += 1
        else:
            game_over = True
            break
    if game_over:
        break
    elif food_eaten >= 10:
        break

if game_over:
    teritory[snake_pos[0]][snake_pos[1]] = "."
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_eaten}")
for r in teritory:
    print(*r,sep="")