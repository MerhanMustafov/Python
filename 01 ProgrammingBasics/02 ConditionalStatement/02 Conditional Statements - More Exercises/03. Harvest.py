# •	1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# •	2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# •	3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# •	4ти ред: брой работници – цяло число в интервала [1 … 20]
from math import floor
from math import ceil
x_sq_m = int(input())
y_grapes_sq_m = float(input())
z_needed_liter_per_wine = int(input())
number_of_workers = int(input())
totall_grasp = x_sq_m * y_grapes_sq_m
wine = (0.4 * totall_grasp) / 2.5
if wine >= z_needed_liter_per_wine:
    wine = wine
    left_wine = wine - z_needed_liter_per_wine
    per_person = left_wine / number_of_workers
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(left_wine)} liters left -> {ceil(per_person)} liters per person.')
elif wine < z_needed_liter_per_wine:
    wine = wine
    lacking_wine = z_needed_liter_per_wine - wine
    print(f'It will be a tough winter! More {floor(lacking_wine)} liters wine needed.')
