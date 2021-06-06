numbers = input().split("|")
new_num = []
for n in reversed(numbers):
    for x in n.split():
        if not x == " ": #or if x != " ":
            new_num.append(x)
print(*new_num, sep=" ")
# result = (' '.join([i for sub in input().split("|")[::-1]for i in sub.split() if i != " "]))
# print(result)









