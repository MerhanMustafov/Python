initial_number = int(input())
number_to_list = [int(x) for x in str(initial_number)]
number_to_list.sort(reverse=True)
length = len(number_to_list)

for element in range(0, length):
    print(number_to_list[element], end='')