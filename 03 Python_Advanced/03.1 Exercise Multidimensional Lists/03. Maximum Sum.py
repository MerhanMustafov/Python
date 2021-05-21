def filling_the_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append([int(el) for el in input().split()])

    return matrix
rows, cols = input().split()
matrix = filling_the_matrix(int(rows))

best_matrix = []
best_sum = -1

for row_ind in range(int(rows) - 2):
    for col_ind in range(int(cols)- 2):
        cur_matrix = [matrix[row_ind][col_ind: col_ind+3],
                      matrix[row_ind+1][col_ind: col_ind+3],
                      matrix[row_ind+2][col_ind: col_ind+3]]

        cur_sum = sum([sum(el) for el in cur_matrix])
        if cur_sum > best_sum:
            best_sum = cur_sum
            best_matrix = cur_matrix

print(f"Sum = {best_sum}")
for r in range(len(best_matrix)):
    # print(" ".join([str(num) for num in best_matrix[r]]))
    print(*best_matrix[r], sep=" ")

