initial_items = input().split(", ")

command = input()
while not command == "Craft!":
    type_command, item = command.split(" - ")

    if type_command == "Collect":
        if item not in initial_items:
            initial_items.append(item)
    elif type_command == "Drop":
        if item in initial_items:
            initial_items.remove(item)
    elif type_command == "Combine Items":
        command = item
        old, new = command.split(":")
        if old in initial_items:
            index = initial_items.index(old)
            initial_items.insert(index+1, new)
    elif type_command == "Renew":
        if item in initial_items:
            position = initial_items.index(item)
            initial_items.pop(position)
            initial_items.append(item)

    command = input()
print(*initial_items, sep=", ")