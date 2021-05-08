# n = int(input())
# from math import fabs
# from math import floor
# sum_first = 0
# sum_second = 0
#
# for number in range(1, n + 1):
#     value = int(input())
#     sum_first += value
# for number in range(1, n + 1):
#     value = int(input())
#     sum_second += value
# if sum_first == sum_second:
#     print(f'Yes, sum = {sum_first}')
# else:
#     print(f'No, diff = {floor(fabs(sum_first - sum_second))}')

n = int(input())
sum_first = 0
sum_second = 0
for numbers in range (1, n+1):
    value = int(input())
    sum_first += value
for numbers in range (1, n+1):
    value = int(input())
    sum_second += value
if sum_first == sum_second:
    print(f'Yes, sum = {sum_first}')
else:
    print(f'No, diff = {abs(sum_first - sum_second)}')