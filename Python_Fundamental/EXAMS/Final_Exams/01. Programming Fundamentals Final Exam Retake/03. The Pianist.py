n = int(input())
my_dict = {}
for com in range(n):
    com_input = input().split("|")
    piece = com_input[0]
    composure = com_input[1]
    key = com_input[2]
    my_dict[piece] = {"composuare": composure, "key": key}
# print(my_dict)
command = input()
while not command == "Stop":
    command = command.split("|")
    if command[0] == "Add":
        if command[1] not in my_dict.keys():
            my_dict[command[1]] = {"composuare": command[2], "key": command[3]}
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
        else:
            print(f"{command[1]} is already in the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in my_dict.keys():
            my_dict.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in my_dict.keys():
            my_dict[piece]["key"] = command[2]
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
my_dict = dict(sorted(my_dict.items(), key=lambda kvp: (kvp[0], kvp[0][0])))

for p, c in my_dict.items():
    print(f"{p} -> Composer: {c['composuare']}, Key: {c['key']}")


# n = int(input())
# data = {}
# for _ in range(n):
#     command_one = input().split("|")
#     piece = command_one[0]
#     composer = command_one[1]
#     key = command_one[2]
#     data[piece] = {'c': composer, 'k': key}
#
# second_command = input()
# while not second_command == "Stop":
#     second_command = second_command.split("|")
#     p = second_command[1]
#     if second_command[0] == "Add":
#         composer = second_command[2]
#         key = second_command[3]
#         if not p in data:
#             data[p] = {'c': composer, 'k': key}
#             print(f"{p} by {composer} in {key} added to the collection!")
#         else:
#             print(f"{p} is already in the collection!")
#     elif second_command[0] == "Remove":
#         p = second_command[1]
#         if p in data:
#             data.pop(p)
#             print(f"Successfully removed {p}!")
#         else:
#             print(f"Invalid operation! {p} does not exist in the collection.")
#     elif second_command[0] == "ChangeKey":
#         p = second_command[1]
#         new_key = second_command[2]
#         if p in data:
#             data[p]['k'] = new_key
#             print(f"Changed the key of {p} to {new_key}!")
#         else:
#             print(f"Invalid operation! {p} does not exist in the collection.")
#     second_command = input()
# data = sorted(data.items(), key=lambda kdv: (kdv[0], kdv[1]['c']))
# for kkeyy, dict in data:
#     print(f"{kkeyy} -> Composer: {dict['c']}, Key: {dict['k']}")


