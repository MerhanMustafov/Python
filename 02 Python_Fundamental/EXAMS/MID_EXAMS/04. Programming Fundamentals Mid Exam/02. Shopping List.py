initial_list = input().split("!")

command = input()
while not command == "Go Shopping!":
    split = command.split()
    if len(split) > 2:
        typee, item, item_2 = command.split()
    else:
        typee, item = command.split()

    if typee == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)
        pass
    elif typee == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)
        pass
    elif typee == "Correct":
        old_item = item
        new_item = item_2
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item

    elif typee == "Rearrange":
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)


    command = input()

print(*initial_list, sep=", ")
