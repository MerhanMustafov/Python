targets = list(map(int, input().split()))

command = input()
while not command == "End":
    typee, index, power_value_radious = command.split()
    index = int(index)
    power_value_radious = int(power_value_radious)
    if typee == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= power_value_radious
            if targets[index] <= 0:
                targets.pop(index)

    elif typee == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, power_value_radious)
        else:
            print("Invalid placement!")

    elif typee == "Strike":
        start = index - power_value_radious
        end = index + power_value_radious
        if start >= 0 and end < len(targets):
            del targets[start:end + 1]
        else:
            print("Strike missed!" )

    command = input()
targets = list(map(str, targets))
print("|".join(targets))

# targets = [int(x) for x in input().split()]
#
# command = input()
# while not command == "End":
#     command = command.split()
#     type_com = command[0]
#     if type_com == "Shoot":
#         index = int(command[1])
#         power = int(command[2])
#         if 0 <= index < len(targets):
#             targets[index] -= power
#             if targets[index] <= 0:
#                 targets.pop(index)
#     elif type_com == "Add":
#         index = int(command[1])
#         value = int(command[2])
#         if 0 <= index < len(targets):
#             targets.insert(index, value)
#         else:
#             print("Invalid placement!")
#     elif type_com == "Strike":
#         index = int(command[1])
#         radios = int(command[2])
#         start = index - radios
#         end = index + radios
#         if (0 <= start) and (end < len(targets)):
#             del targets[start:end+1]
#         else:
#             print("Strike missed!")
#     command = input()
# targets = [str(y) for y in targets]
# print("|".join(targets))