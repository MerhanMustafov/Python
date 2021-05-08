pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]

max_health_cap = int(input())

command = input()

while not command == "Retire":
    type_command = command.split()
    if type_command[0] == "Fire":
        index = int(type_command[1])
        damage = int(type_command[2])
        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit(0)
    elif type_command[0] == "Defend":
        start_ind = int(type_command[1])
        end_ind = int(type_command[2])
        damage = int(type_command[3])
        if (0 <= start_ind < len(pirate_ship))  and  (0 <= end_ind < len(pirate_ship)):
            for el in range(start_ind, end_ind+1):
                pirate_ship[el] -= damage
                if pirate_ship[el] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit(0)
    elif type_command[0] == "Repair":
        index = int(type_command[1])
        health = int(type_command[2])
        if 0 <= index < len(pirate_ship):
            if pirate_ship[index] > max_health_cap:
                pirate_ship[index] = max_health_cap
                command = input()
                continue
            if pirate_ship[index] + health > max_health_cap:
                pirate_ship[index] = max_health_cap
                command = input()
                continue
            pirate_ship[index] += health
    elif type_command[0] == "Status":
        count = 0
        for number in pirate_ship:
            if number < (max_health_cap * 0.2):
                count += 1
        print(f"{count} sections need repair.")


    command = input()
sum_pirate_ship = sum(pirate_ship)
sum_war_ship = sum(war_ship)
print(f"Pirate ship status: {sum_pirate_ship}")
print(f"Warship status: {sum_war_ship}")

