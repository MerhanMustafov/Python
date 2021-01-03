capacity_luggage = float(input())

luggage_number = 0
no_more_space = False
command = input()

while command != 'End':
    current_luggage = float(command)
    if current_luggage > capacity_luggage:
        no_more_space = True
        break
    luggage_number += 1
    if luggage_number % 2 == 0:
        capacity_luggage -= current_luggage * 1.1
        command = input()
        continue
    capacity_luggage -= current_luggage
    command = input()

if command == 'End':
    print("Congratulations! All suitcases are loaded!")
if no_more_space:
    print("No more space!")
print(f"Statistic: {luggage_number} suitcases loaded.")
