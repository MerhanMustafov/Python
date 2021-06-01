# numbers = input().split("|")
# # print(numbers)
# # [[print('  '.join(x), end="") for x in n if x.isdigit()]for n in reversed(numbers)]
# new_num = []
# for n in reversed(numbers):
#     for x in n:
#         if x.isnumeric():
#             new_num.append(x)
#             # print(x, end=" ")
# print(*new_num, sep=" ")

# regular_list = input().split("|")
# flat_list = [item for sublist in reversed(regular_list)for item in sublist if item.isdigit()]
# # print('Original list', regular_list)
# print(' '.join(flat_list))

result = [' '.join(list_as_string.split())for list_as_string in input().split("|")[::-1]]
print(*result, sep=" ")









