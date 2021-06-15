
board_size = int(input())
bombs_number = int(input())
BOMBA = "*"
EMPTY = "0"
board = [[int(el) for el in EMPTY * board_size] for ele in range(board_size)]


def bombs_positions():
    bomb_coordinates = []
    for position in range(bombs_number):
        data = input()
        cord = [el for el in data if el.isnumeric()]
        cord = [int(el) for el in cord]
        bomb_coordinates.append(cord)
    return bomb_coordinates


bomb_list = bombs_positions()


def making_the_table_with_bombs():
    for bomb in bomb_list:
        bomb_row, bomb_col = bomb[0], bomb[1]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == bomb_row and c == bomb_col:
                    board[r][c] = BOMBA

    return board


boarda = making_the_table_with_bombs()
deltas = [
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1),
]
number = 0
for row in range(len(boarda)):
    for column in range(len(boarda[0])):
        current_row = row
        current_col = column
        current_index = boarda[current_row][current_col]
        if not current_index == BOMBA:
            for delt in deltas:
                delta_row, delta_col = delt[0], delt[1]
                delta_row_index, delta_col_index = delta_row + current_row, delta_col + current_col
                if 0 <= delta_row_index < len(boarda) and 0 <= delta_col_index < len(boarda):
                    for el in bomb_list:
                        bob_row = el[0]
                        bob_col = el[1]
                        if delta_row_index == bob_row and delta_col_index == bob_col:
                            number += 1
                            break
            boarda[current_row][current_col] = number
            number = 0
sus = []
for i in range(len(boarda)):
    result = ''
    for el in range(len(boarda[i])):
        result += str(boarda[i][el])
        if el < len(boarda) - 1:
            result += " "
    sus.append(result)

for el in sus:
    print(el)



