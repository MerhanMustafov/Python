command = input()
lines = 1
lst = []
dictionary = {}
while not command == "stop":
    lst.append(command)
    if lines % 2 == 0:
        if lst[lines-2] in dictionary:
            dictionary[lst[lines-2]] +=  int(lst[lines-1])
        else:
            dictionary[lst[lines-2]] = int(lst[lines-1])

    lines += 1
    command = input()
for key, value in dictionary.items():
    print(f"{key} -> {dictionary[key]}")