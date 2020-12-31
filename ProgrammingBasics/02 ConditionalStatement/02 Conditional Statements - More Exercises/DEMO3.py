from math import floor
from math import  ceil

area = int(input())
grapes_for_meter = float(input())
wine_needed = int(input())
workers = int(input())
liter_of_wine = 2.5

all_grape = area * grapes_for_meter
total_wine = all_grape / 2.5 - all_grape / 2.5 * 60 / 100

if total_wine >= wine_needed:
    liter_left = total_wine - wine_needed
    per_person = liter_left / workers
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    print(f"{ceil(liter_left)} liters left -> {ceil(per_person)} liters per person.")
else:
    liters_needed = wine_needed - total_wine
    print(f"It will be a tough winter! More {floor(liters_needed)} liters wine needed.")