number = input()
total = []

for digit in str(number):
    total.append(int(digit))

total.sort(reverse=True)

for i in range(len(total)):
    print(total[i], end='')

# number_input = input()
# number_max = ""
# number_input_str = str(number_input)
# count_digits = len(number_input_str)
# rest_digits = number_input_str
#
# for digit_position in range(count_digits):
#     max_digit = 0
#     max_poss = 0
#     for i in range(len(rest_digits)):
#         if int(rest_digits[i]) > max_digit:
#             max_digit = int(rest_digits[i])
#             max_poss = i
#
#     number_max += str(max_digit)
#     rest_digits = rest_digits[:max_poss] + rest_digits[max_poss + 1:]
#
# print(int(number_max))

