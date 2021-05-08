n = int(input())
new_lst = []
count = 0
for line in range(n):
    row = input().split()
    row = list(map(int, row))
    new_lst.append(row)

squares = input().split()
for index in squares:
    row, col = index.split("-")
    row = int(row)
    col = int(col)
    checking_lst = new_lst[row]

    for _ in range(len(checking_lst)):
        if checking_lst[col] > 0:
            checking_lst[col] -= 1
            if checking_lst[col] == 0:
                count += 1

        break


print(count)
