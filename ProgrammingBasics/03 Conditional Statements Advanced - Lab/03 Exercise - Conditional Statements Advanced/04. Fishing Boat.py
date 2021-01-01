# 	Бюджет на групата – цяло число;
# 	Сезон –  текст: "Spring", "Summer", "Autumn" или "Winter";
# 	Брой рибари – цяло число.
from math import fabs
budget = int(input())
season = input()
fisher_number = int(input()) # fisher_number % 2 == 0:

rent_boat = 0
even = fisher_number % 2 == 0
# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.

if season == "Spring":
    rent_boat = 3000
    if fisher_number <= 6:
        rent_boat *= 0.9
    elif 6 < fisher_number <= 11:
        rent_boat *= 0.85
    elif fisher_number > 11:
        rent_boat *= 0.75
    if even:
        rent_boat *= 0.95
elif season == "Summer":
    rent_boat = 4200
    if fisher_number <= 6:
        rent_boat *= 0.9
    elif 6 < fisher_number <= 11:
        rent_boat *= 0.85
    elif fisher_number > 11:
        rent_boat *= 0.75
    if even:
        rent_boat *= 0.95
elif season == "Winter":
    rent_boat = 2600
    if fisher_number <= 6:
        rent_boat *= 0.9
    elif 6 < fisher_number <= 11:
        rent_boat *= 0.85
    elif fisher_number > 11:
        rent_boat *= 0.75
    if even:
         rent_boat *= 0.95
elif season == "Autumn":
    rent_boat = 4200
    if fisher_number <= 6:
        rent_boat *= 0.9
    elif 6 < fisher_number <= 11:
        rent_boat *= 0.85
    elif fisher_number > 11:
        rent_boat *= 0.75

if budget >= rent_boat:
    print(f"Yes! You have {budget - rent_boat:.2f} leva left.")
elif budget < rent_boat:
    print(f"Not enough money! You need {fabs(rent_boat - budget):.2f} leva.")
