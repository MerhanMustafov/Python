my_current_energy = int(input())

command = input()
count_successful_wins = 0
while not command == "End of battle":

    distance_energy = int(command)
    if my_current_energy < distance_energy:
        print(f"Not enough energy! Game ends with {count_successful_wins} won battles and {my_current_energy} energy")
        exit(0)
    my_current_energy -= distance_energy
    count_successful_wins += 1

    if count_successful_wins % 3 == 0 and not count_successful_wins == 0:
        my_current_energy += count_successful_wins

    command = input()

print(f"Won battles: {count_successful_wins}. Energy left: {my_current_energy}")


# energy_status = int(input())
#
# command = input()
# won_battles = 0
# while not command == "End of battle" and energy_status > 0:
#     number = int(command)
#     if energy_status - number < 0:
#         print(f"Not enough energy! Game ends with {won_battles} won battles and {energy_status} energy")
#         exit(0)
#     energy_status -= number
#     won_battles += 1
#     if won_battles % 3 == 0 and not won_battles == 0:
#         energy_status += won_battles
#
#     command = input()
# if command == "End of battle":
#     print(f"Won battles: {won_battles}. Energy left: {energy_status}")
# elif energy_status <= 0:
#     print(f"Not enough energy! Game ends with {won_battles} won battles and {energy_status} energy")