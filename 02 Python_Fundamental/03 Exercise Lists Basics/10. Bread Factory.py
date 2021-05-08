day_events_list = input().split("|")

MAX_ENERGY = 100
ORDER_ENERGY = 30
REST_ENERGY = 50
current_energy = 100
current_coins = 100
is_not_bankrupt = True

for event in day_events_list:
    single_events_list = event.split("-")
    name = single_events_list[0]
    value = int(single_events_list[1])

    if name == "rest":
        gained_energy = 0

        if current_energy + value > MAX_ENERGY:
            gained_energy = MAX_ENERGY - current_energy
            current_energy = MAX_ENERGY
        else:
            current_energy += value
            gained_energy = value

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif name == "order":
        if current_energy >= ORDER_ENERGY:
            current_energy -= ORDER_ENERGY
            current_coins += value
            print(f"You earned {value} coins.")
        else:
            current_energy += REST_ENERGY
            print("You had to rest!")
            continue

    else:
        if current_coins > value:
            current_coins -= value
            print(f"You bought {name}.")
        else:
            print(f"Closed! Cannot afford {name}.")
            is_not_bankrupt = False
            break

#        if coins <= 0:
#            is_not_bankrupt = False
#            break

if is_not_bankrupt:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")