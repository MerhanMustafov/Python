from collections import deque
quantity = int(input())
queue = deque()
names = input()
while not names == "Start":
    queue.append(names)
    names = input()

command = input()
while not command == "End":
    if command.isdigit():
        if quantity >= int(command):
            quantity -= int(command)
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait" )
    elif not command[0].isdigit():
        command = command.split()
        if command[0] == "refill":
            quantity += int(command[1])

    command = input()

print(f"{quantity} liters left")