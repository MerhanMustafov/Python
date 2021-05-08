targets = [int(x) for x in input().split()]

command = input()
while not command == "End":
    type_command, index, value = command.split()
    index = int(index)
    value = int(value)
    if type_command == "Shoot":
        power = value
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif type_command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")
    elif type_command == "Strike":
        radius = value
        if len(targets[:index]) >= radius and len(targets[index:])>= radius:
            start = index - radius
            end = index + radius
            del targets[start:end+1]
        else:
            print("Strike missed!")
    command = input()
print(*targets, sep="|")