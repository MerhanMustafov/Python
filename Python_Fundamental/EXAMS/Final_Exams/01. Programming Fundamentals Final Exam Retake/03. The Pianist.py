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
        if piece in my_dict.keys():
            my_dict[piece]["key"] = command[2]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
my_dict = dict(sorted(my_dict.items(), key=lambda kvp: (kvp[0], kvp[0][0])))

for p, c in my_dict.items():
    print(f"{p} -> Composer: {c['composuare']}, Key: {c['key']}")


