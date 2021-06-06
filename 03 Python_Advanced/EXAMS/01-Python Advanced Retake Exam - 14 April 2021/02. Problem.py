def read_matrix(n):
    return [input().split() for row in range(n)]

data = {name: {"score": 501, 'trows': 0} for name in input().split(", ")}
matrix = read_matrix(7)

current_player = None
there_is_a_winner = False

while not there_is_a_winner:
    for player, dict in data.items():
        current_player = player

        row_col = tuple(int(x) for x in input() if x.isdigit())
        data[player]['trows'] += 1
        if not (0 <= row_col[0] < 7) or not (0 <= row_col[1] < 7):
            continue

        elif matrix[row_col[0]][row_col[1]].isdigit():
            data[player]['score'] -= int(matrix[row_col[0]][row_col[1]])

        elif matrix[row_col[0]][row_col[1]] == "D":
            data[player]['score'] -= (int(matrix[row_col[0]][0]) + int(matrix[row_col[0]][-1])
                                      + int(matrix[0][row_col[1]]) + int(matrix[-1][row_col[1]])) * 2

        elif matrix[row_col[0]][row_col[1]] == "T":
            data[player]['score'] -= (int(matrix[row_col[0]][0]) + int(matrix[row_col[0]][-1])
                                      + int(matrix[0][row_col[1]]) + int(matrix[-1][row_col[1]])) * 3

        elif matrix[row_col[0]][row_col[1]] == "B":
            there_is_a_winner = True
            break

        if data[player]['score'] <= 0:
            there_is_a_winner = True
            break

print(f"{current_player} won the game with {data[current_player]['trows']} throws!")

