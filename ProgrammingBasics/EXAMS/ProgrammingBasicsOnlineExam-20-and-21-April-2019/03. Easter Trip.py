destination = input()
date = input()
nights = int(input())
price = 0
if destination == "France":
    if date == "21-23":
        price = nights * 30
    elif date == "24-27":
        price = nights * 35
    elif date == "28-31":
        price = nights * 40
elif destination == "Italy":
    if date == "21-23":
        price = nights * 28
    elif date == "24-27":
        price = nights * 32
    elif date == "28-31":
        price = nights * 39
elif destination == "Germany":
    if date == "21-23":
        price = nights * 32
    elif date == "24-27":
        price = nights * 37
    elif date == "28-31":
        price = nights * 43
print(f"Easter trip to {destination} : {price:.2f} leva.")