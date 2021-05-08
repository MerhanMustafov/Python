capacity_lugguage = float(input())
command = input()
loaded_lugguage = 0
no_more_space = False
while command != 'End':
    volume_lugguge = float(command)
    if loaded_lugguage % 2 == 0:
        if loaded_lugguage == 0:
            volume_lugguge = volume_lugguge
        else:
            volume_lugguge *= 1.1
    if volume_lugguge >= capacity_lugguage:
        no_more_space = True
        print("No more space!")
        break
    capacity_lugguage -= volume_lugguge
    loaded_lugguage += 1
    command = input()
if command == 'End':
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {loaded_lugguage} suitcases loaded.")