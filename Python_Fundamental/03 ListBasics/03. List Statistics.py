n = int(input())
lst_p = []
count_p = 0
lst_n = []
sum_n = 0

for x in range(n):
    number = int(input())
    if number < 0:
        lst_n.append(number)
        sum_n += number
    elif number >= 0:
        lst_p.append(number)
        count_p += 1
print(lst_p)
print(lst_n)
print(f"Count of positives: {count_p}. Sum of negatives: {sum_n}")


