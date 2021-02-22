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