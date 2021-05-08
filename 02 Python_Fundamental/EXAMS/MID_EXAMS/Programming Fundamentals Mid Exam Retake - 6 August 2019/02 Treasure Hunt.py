initial_loot = input().split("|")

command = input()
while not command == "Yohoho!":
    command = command.split()
    type_command = command[0]

    if type_command == "Loot":
        items = command[1:]
        [initial_loot.insert(0, x) for x in items if not x in initial_loot]

    elif type_command == "Drop":
        index = int(command[1])
        if 0 <= index < len(initial_loot):
            value = initial_loot[index]
            initial_loot.pop(index)
            initial_loot.append(value)
    elif type_command == "Steal":
        count = int(command[1])
        print(*initial_loot[-count:], sep=", ")
        del initial_loot[-count:]
    command = input()

average = 0
for el in initial_loot:
    average += len(el)
if initial_loot:
    final = average / len(initial_loot)
    print(f"Average treasure gain: {final:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")