n = int(input())
max = 0
sum = 0
for number in range(1, n+1):
    num = int(input())
    sum += num
    if number == 1:
        max = num
    elif number > 1:
        if number > max:
            max = num
if sum - max == max:
    print('Yes')
    print(f'Sum = {max}')
else:
    print('No')
    print(f'Diff = {abs(max - (sum - max))}')

# import sys
# n = int(input())
# sum = 0
# max_number = -sys.maxsize
# for number in range (1, n + 1):
#     new_number = int(input())
#     sum += new_number
#     if new_number > max_number:
#         max_number = new_number
#
# if max_number == sum - max_number:
#     print('Yes')
#     print(f'Sum = {max_number}')
# else:
#     difference = max_number - (sum - max_number)
#     print('No')
#     print(f'Diff = {abs(difference)}')
#
