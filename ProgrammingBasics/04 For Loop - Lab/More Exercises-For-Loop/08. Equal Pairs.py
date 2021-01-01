import sys
n = int(input())
current_number = 0
previous_number = 0
equal = 0
max_diff = -sys.maxsize
is_number = True
for i in range(1, 2*n+1):
    number = int(input())
    if n == 1:
        if i == 1:
            current_number += number
            previous_number = current_number
            current_number = 0
            continue
        elif i == 2:
            current_number += number
            if current_number == previous_number:
                previous_number = current_number + previous_number
            else:
                is_number = False
                max_diff = abs(previous_number - current_number)
                break
    if i % 2 != 0:
        current_number += number
    if i == 2:
        current_number += number
        previous_number = current_number
        current_number = 0
        continue
    if i % 2 == 0:
        current_number += number
        if current_number == previous_number:
            current_number = 0

        else:
            if current_number != previous_number:
                is_number = False
                diff = abs(previous_number - current_number)
                if diff > max_diff:
                    max_diff = diff
                else:
                    max_diff = max_diff
                previous_number = current_number
                current_number = 0


if is_number:
    print(f"Yes, value={previous_number}")
elif is_number == False:
    print(f"No, maxdiff={max_diff}")



#
# n = int(input())
# value = True
# current_number = 0
# previous_number = 0
#
# bigest_difference_between_two_number = 0
#
# for numbers in range(1, 2 * n + 1):
#     number = int(input())
#
#     if numbers % 2 == 0:
#         current_number += number
#         if numbers == 2:
#             previous_number = current_number
#             current_number = 0
#         else:
#             if previous_number == current_number:
#                 current_number = 0
#             else:
#                 value = False
#             difference_between_two_number = abs(current_number - previous_number)
#             if difference_between_two_number > bigest_difference_between_two_number:
#                 bigest_difference_between_two_number = abs(difference_between_two_number)
#                 previous_number = current_number
#                 current_number = 0
#
#     else:
#         current_number += number
#
# if value:
#     print(f"Yes, value = {previous_number}")
# if not value:
#     print(f"No, maxdiff = {bigest_difference_between_two_number}" )