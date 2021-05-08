initial_array = list(map(int, input().split()))

command = input()
while not command == "end":
    type_command = command.split()
    if len(type_command) > 1:
        index_one = int(type_command[1])
        index_two = int(type_command[2])
    if type_command[0] == "swap":
        initial_array[index_one], initial_array[index_two] = initial_array[index_two], initial_array[index_one]
    elif type_command[0] == "multiply":
        initial_array[index_one] *= initial_array[index_two]
    elif type_command[0] == "decrease":
        initial_array = [num - 1 for num in initial_array]

    command = input()
print(*initial_array, sep=", ")

# initial_values = [int(x) for x in input().split()]
#
# command = input()
# while not command == "end":
#     command = command.split()
#     if command[0] == "swap":
#         initial_values[int(command[1])], initial_values[int(command[2])] = initial_values[int(command[2])], initial_values[int(command[1])]
#     elif command[0] == "multiply":
#         initial_values[int(command[1])] *= initial_values[int(command[2])]
#     elif command[0] == "decrease":
#         initial_values = [num - 1 for num in initial_values]
#
#     command = input()
# print(", ".join([str(b) for b in initial_values]))