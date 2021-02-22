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
