string = input()
str = string.split()
lst = []
for n in range(len(str)):
    number = int(str[n])
    if number < 0:
        positive_n = abs(number)
        lst.append(positive_n)
    else:
        negative_n = -number
        lst.append(negative_n)
print(lst)