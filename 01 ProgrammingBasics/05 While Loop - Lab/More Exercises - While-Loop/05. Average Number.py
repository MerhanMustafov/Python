n = int(input())
sum = 0
count = 0

for numbers in range(n):
    new_num = int(input())
    sum += new_num
    count += 1
average = sum / count
print(f'{average:.2f}')