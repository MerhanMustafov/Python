first_command = input()
data = {}
while not first_command == "Sail":
    first_command = first_command.split("||")
    city = first_command[0]
    population = int(first_command[1])
    gold = int(first_command[2])
    if city not in data.keys():
        data[city] = {'p': population, 'g': gold}
    else:
        data[city]['p'] += population
        data[city]['g'] += gold
    # print(data)
    first_command = input()

second_command = input()
while not second_command == "End":
    second_command = second_command.split("=>")
    command = second_command[0]
    town = second_command[1]
    if command == "Plunder":
        people = int(second_command[2])
        gold = int(second_command[3])
        data[town]['p'] -= people
        data[town]['g'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if data[town]['p'] <= 0 or data[town]['g'] <= 0:
            data.pop(town)
            print(f"{town} has been wiped off the map!")
    elif command == "Prosper":
        gold = int(second_command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            second_command = input()
            continue
        data[town]['g'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {data[town]['g']} gold.")

    second_command = input()

count = len(data.keys())
data = sorted(data.items(), key=lambda kdv: (-kdv[1]['g'], kdv[0]))
print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
for name, p_g in data:
    print(f"{name} -> Population: {p_g['p']} citizens, Gold: {p_g['g']} kg")