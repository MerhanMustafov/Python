gidts_name = input()
lst = gidts_name.split(" ")
command = input()
while command != "No Money":
    current_lst = command.split()
    index = 0
    if "OutOfStock" in current_lst:
        for i in range (len(lst)):
            if lst[i] == current_lst[1]:
                lst[i] = str(None)
    elif "Required" in current_lst:
        for i in range(len(lst)):
            if str(i) == current_lst[2]:
                current_gift = current_lst[1]
                lst[i] = str(current_gift)

    elif "JustInCase" in command:
        lst[-1] = str(current_lst[1])

    command = input()
if str(None) in lst:
    for i in range(len(lst) -1, -1, -1):
        word = lst[i]
        if lst[i] == str(None):
            lst.remove(word)
print(" ".join(lst))
