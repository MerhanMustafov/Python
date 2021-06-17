from collections import deque


def list_manipulator(*args):
    lst = args[0]
    command = args[1]
    position = args[2]
    if len(args) > 3:
        numbers = deque(args[3:])

        if command == "add" and position == "beginning":
            while numbers:
                lst.insert(0, numbers.pop())
        elif command == "add" and position == "end":
            while numbers:
                lst.append(numbers.popleft())
        elif command == "remove" and position == "beginning":
            lst = lst[numbers[0]:]
        elif command == "remove" and position == "end":
            lst = lst[:-numbers[0]]
    else:
        if command == "remove" and position == "end":
            lst = lst[0:len(lst)-1]
        if command == "remove" and position == "beginning":
            lst = lst[1:]
    return lst

# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
# print(list_manipulator([1,2,3], "remove", "end", 2))
# print(list_manipulator([1,2,3], "remove", "beginning", 2))
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

