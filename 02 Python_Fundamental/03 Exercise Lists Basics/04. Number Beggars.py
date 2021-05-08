string = input()
num_beggers = int(input())

money_lst = string.split(", ")
BEGGERS = num_beggers

repeat = 0
lst = []
lst_position = 0

for a in range(len(money_lst)):
    money = int(money_lst[a])
    if num_beggers == 0 and len(money_lst) > a:
        num_beggers = BEGGERS
        lst_position = 0

    num_beggers -= 1
    if repeat == BEGGERS:
        num = lst[lst_position]
        sum = num + money
        lst[lst_position] = sum
        lst_position += 1
        continue
    lst.append(money)
    repeat += 1

if BEGGERS > len(money_lst):
    times = BEGGERS - len(money_lst)
    for i in range(times):
        lst.append(0)
print(lst)



