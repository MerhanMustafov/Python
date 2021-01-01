n = int(input())
even_sum = 0
odd_sum = 0

for numbers in range (0, n):
    input_number = int(input())
    if numbers % 2 == 0:
        even_sum += input_number
    else:
        odd_sum += input_number
if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print(f'Diff = {abs(even_sum - odd_sum)}')
# import math
# n = int(input())
# sum_even = 0
# sum_odd = 0
#
# for number in range (1, n + 1):
#     value = (int(input()))
#     if number % 2 == 0:
#         sum_even += value
#     else:
#         sum_odd += value
# if sum_even == sum_odd:
#     print('Yes')
#     print(f'Sum = {sum_odd}')
# else:
#     print('No')
#     print(f'Diff = {math.floor(math.fabs(sum_even - sum_odd))}')
