
string = list(map(str, input()))

numbers = []
for element in string:
    if element.isdigit():
        numbers.append(int(element))
# for el in reversed(string):
#     if el.isdigit():
#         string.remove(el)
removing_digits = [string.remove(el) for el in reversed(string) if el.isdigit()]
take_lst = [numbers[index] for index in range(len(numbers)) if index % 2 == 0 ]
# for index in range(len(numbers)):
#     if index % 2 == 0:
#         take_lst.append(numbers[index])
#     else:
skip_lst = [numbers[index] for index in range(len(numbers)) if not index % 2 == 0]
non_numbers = string
final = []
skip_count = 0
for  take, skip in zip(take_lst, skip_lst):
    # string[:take] = []

    skipped = non_numbers[:skip_count] = []
    taken = non_numbers[:take]
    final.append(taken)

    skip_count += skip
print("".join(str(final)))
    #
    # skipped = string[:] =[]
    # print(taken, skipped)

a=0