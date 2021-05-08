fuel = str(input())
number = float(input())
if number >= 25:
    if fuel == 'Diesel':
        print(f"You have enough {'diesel'}.")
    elif fuel == "Gasoline":
        print(f"You have enough {'gasoline'}.")
    elif fuel == "Gas":
        print(f"You have enough {'gas'}.")
    else:
        print('Invalid fuel!')
elif number < 25:
    if fuel == 'Diesel':
       print(f"Fill your tank with {'diesel'}!")
    elif fuel == "Gasoline":
        print(f"Fill your tank with {'gasoline'}!")
    elif fuel == "Gas":
        print(f"Fill your tank with {'gas'}!")
    else:
        print('Invalid fuel!')