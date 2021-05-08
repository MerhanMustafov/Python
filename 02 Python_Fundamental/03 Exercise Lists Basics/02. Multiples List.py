factor = int(input())
count = int(input())
lst = []
dividend = factor
while len(lst) < count:

    while dividend % factor == 0 and len(lst) < count:
        lst.append(dividend)
        dividend += 1
    dividend += 1

print(lst)