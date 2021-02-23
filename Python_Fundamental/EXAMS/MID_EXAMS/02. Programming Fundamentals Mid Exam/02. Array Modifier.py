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
