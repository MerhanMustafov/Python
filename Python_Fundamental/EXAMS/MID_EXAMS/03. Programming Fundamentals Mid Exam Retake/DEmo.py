statu_pirate_ship = [int(x) for x in input().split(">")]
status_war_ship = [int(x) for x in input().split(">")]

max_health_cap = int(input())

command = input()
is_pirate_ship_won = False
is_war_ship_won = False
while not command == "Retire":
    command = command.split()
    type_com = command[0]

    if type_com == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_war_ship):
            status_war_ship[index] -= damage
            if status_war_ship[index] <= 0:
                is_pirate_ship_won = True
                break

    elif type_com == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if (0 <= start_index < len(statu_pirate_ship)) and (0 <= end_index < len(statu_pirate_ship)):
            for section in range(len(statu_pirate_ship)):
                if start_index <= section <= end_index:
                    statu_pirate_ship[section] -= damage
                    if statu_pirate_ship[section] <= 0:
                        is_war_ship_won = True
                        break

    elif type_com == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(statu_pirate_ship):
            if statu_pirate_ship[index] + health < max_health_cap:
                statu_pirate_ship[index] += health
            else:
                statu_pirate_ship[index] = max_health_cap

    elif type_com == "Status":
        count = 0
        percent = int(max_health_cap * 0.2)
        for section in range (len(statu_pirate_ship)):
            if statu_pirate_ship[section] < percent:
                count += 1
        print(f"{count} sections need repair.")


    command = input()


if is_pirate_ship_won:
    print("You won! The enemy ship has sunken.")
elif is_war_ship_won:
    print("You lost! The pirate ship has sunken.")

else:
    print(f"Pirate ship status: {sum(statu_pirate_ship)}")
    print(f"Warship status: {sum(status_war_ship)}")