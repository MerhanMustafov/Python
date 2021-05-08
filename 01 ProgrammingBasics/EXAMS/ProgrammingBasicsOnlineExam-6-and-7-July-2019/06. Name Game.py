name = input()
points = 0
most_points = 0
name_best = name
while name != 'Stop':
    for letter in range (len(name)):
        number = int(input())
        position = name[letter]
        value = ord(position)
        if number == value:
            points += 10
        else:
            points += 2
    if points >= most_points:
        most_points = points
        name_best = name
    points = 0
    name = input()
print(f"The winner is {name_best} with {most_points} points!")