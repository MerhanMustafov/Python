n = int(input())
check = []
unbalanced = False
balanced = False
count = 0
for line in range(n):
    str = input()
    check.append(str)
    if str == "(" or str == ")" or str == "( ":
        count += 1

if count % 2 != 0:
    print("UNBALANCED")
else:
    for l in range(n):
        if check[l] == check[l - 1]:
            unbalanced = True
        else:
            balanced = True
if unbalanced:
    print("UNBALANCED")
elif balanced:
    print("BALANCED")


