from math import fabs

budget = int(input())
season = input()
fisher_number = int(input())  # fisher_number % 2 == 0:

rent_boat = 0
even = fisher_number % 2 == 0
discount = True

if season == "Spring":
    rent_boat = 3000
    if fisher_number <= 6:
        rent_boat *= 0.9
    elif 7 <= fisher_number <= 11:
        rent_boat *= 0.85
    elif fisher_number >= 12:
        rent_boat *= 0.75
elif season == "Summer":
    rent_boat = 4200
    if fisher_number <= 6:
        rent_boat *= 0.9
    elif 7 <= fisher_number <= 11:
        rent_boat *= 0.85
    elif fisher_number >= 12:
        rent_boat *= 0.75
elif season == "Autumn":
    discount = False
    rent_boat = 4200

    if fisher_number <= 6:
        rent_boat *= 0.9
    elif 7 <= fisher_number <= 11:
        rent_boat *= 0.85
    elif fisher_number >= 12:
        rent_boat *= 0.75
elif season == "Winter":
    rent_boat = 2600
    if fisher_number <= 6:
        rent_boat *= 0.9
    elif 7 <= fisher_number <= 11:
        rent_boat *= 0.85
    elif fisher_number >= 12:
        rent_boat *= 0.75

if discount:
    if even:
        even = rent_boat * 0.95
    else:
        rent_boat = rent_boat

if budget >= rent_boat:
    print(f"Yes! You have {fabs(budget - rent_boat):.2f} leva left.")
elif budget < rent_boat:
    print(f"Not enough money! You need {fabs(rent_boat - budget):.2f} leva.")
