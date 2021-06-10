from collections import deque

def row(x):
    return [x for x in input().split()]

def reading_the_field(n):
    return [row(x) for x in range(n)]

def finding_the_king(field):
    the_king = []
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == "K":
                the_king += [row, col]
    return the_king

def searching_for_checkmates(field, king):
    row = king[0]
    value = king[1]
    z = king[1]
    queens = []
    for x in range(value+1, len(field)):#right
        if field[row][x] == "Q":
            queens.append([row, x])
            break
    for x in range(value, -1, -1):#left
        if field[row][x] == "Q":
            queens.append([row, x])
            break
    for x in range(row + 1, len(field)):#down
        if field[x][value] == "Q":
            queens.append([x, value])
            break
    for x in range(row, -1, -1):#Up
        if field[x][value] == "Q":
            queens.append([x, value])
            break
    for x in range(row, -1, -1):# diagonal UP LEFT
        if field[x][z] == "Q":
            queens.append([x, z])
            break
        elif (z == 0):
            break
        z -= 1
    z = value
    for x in range(row, -1, -1):# Diagonal UP right
        if field[x][z] == "Q":
            queens.append([x, z])
            break
        elif (z == 7):
            break
        z += 1
    z = value
    for x in range(row, 8):# DIAGONAL DOWN RIGHT
        if field[x][z] == "Q":
            queens.append([x, z])
            break
        elif (z == 7):
            break
        z += 1
    z = value
    for x in range(row, 8):# DIAGONAL DOWN LEFT
        if field[x][z] == "Q":
            queens.append([x, z])
            break
        elif (z == 0):
            break
        z -= 1

    return queens


field = reading_the_field(8)
king = finding_the_king(deque(field))

checkmates = searching_for_checkmates(field, king)
if checkmates:
    for abc in checkmates:
        print(abc)
else:
    print(f"The king is safe!")