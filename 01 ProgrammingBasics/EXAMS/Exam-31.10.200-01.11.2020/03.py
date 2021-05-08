num_people = int(input())
season = input()
total = 0
if num_people <= 5:
    if season == 'spring':
        total = num_people * 50
    elif season == 'summer':
        total = num_people * 48.50 * 0.85
    elif season == 'autumn':
        total = num_people * 60
    elif season == 'winter':
        total = num_people * 86 * 1.08
elif num_people > 5:
    if season == 'spring':
        total = num_people * 48
    elif season == 'summer':
        total = num_people * 45 * 0.85
    elif season == 'autumn':
        total = num_people * 49.50
    elif season == 'winter':
        total = num_people * 85 * 1.08
print(f"{total:.2f} leva.")