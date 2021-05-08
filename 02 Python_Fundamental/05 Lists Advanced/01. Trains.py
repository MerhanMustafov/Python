n_carriages = int(input())
carriages = [0] * n_carriages

command = input()

while not command == "End":
    data = command.split()
    if data[0] == "add":
        people = int(data[1])
        carriages[-1] += people
    elif data[0] == "insert":
        index = int(data[1])
        people = int(data[2])
        carriages[index] += people
    elif data[0] == "leave":
        index = int(data[1])
        people = int(data[2])
        carriages[index] -= people
    command = input()

print(carriages)