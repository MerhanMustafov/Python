# lst = [1, 2, 3, 5, 54, 8, 10, 33]
# a = lst.index(max(lst))
# b = min(i for i in lst if i % 2)
# c = lst.index(b)
# print(a, b, c)
def exchange(command, lst):
    index = int(command[1])
    lst = lst[index:] + lst[:index]
    return lst

def min_max(command, lst):
    even_odd = command[1]
    index = 0
    if command[0] == "max":
        if even_odd == "even":
            b = max(i for i in lst if i % 2==0)
            for i in range(len(lst)-1, -1, -1):
                if lst[i] == b:
                    index = i
                    break
        elif even_odd == "odd":
            b = max(i for i in lst if i % 2 != 0)
            for i in range(len(lst) - 1, -1, -1):
                if lst[i] == b:
                    index = i
                    break
    elif command[0] == "min":
        if even_odd == "even":
            b = min(i for i in lst if i % 2 == 0)
            for i in range(len(lst) - 1, -1, -1):
                if lst[i] == b:
                    index = i
                    break
        elif even_odd == "odd":
            b = min(i for i in lst if i % 2 != 0)
            for i in range(len(lst) - 1, -1, -1):
                if lst[i] == b:
                    index = i
                    break
    return index


string = input()
string = [int(string[x]) for x in range(0, len(string), 2)]

command = input()
while not command == "end":
    command = command.split()
    if command[0] == "exchange":
        print(exchange(command, string))
    if command[0] == "max" or command[0] == "min":
        print(min_max(command, string))
    command = input()
