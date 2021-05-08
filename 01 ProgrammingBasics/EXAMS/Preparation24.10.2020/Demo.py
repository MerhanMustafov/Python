easter_breads = int(input())
max_points = 0
best_baker = ''

for kozunak in range(easter_breads):
    baker = input()

    total_points = 0

    command = input()
    while command != 'Stop':
        grade = int(command)
        total_points += grade
        command = input()
    print(f"{baker} has {total_points} points.")
    if total_points > max_points:
        max_points = total_points
        best_baker = baker
        print(f"{baker} is the new number 1!")
print(f"{best_baker} won competition with {max_points} points!")
