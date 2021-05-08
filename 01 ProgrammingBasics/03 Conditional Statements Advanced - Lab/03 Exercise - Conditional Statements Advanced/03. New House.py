from math import fabs
type_flowers = input()
number = int(input())
budget = int(input())


price = 0
total_sum = 0
if type_flowers == "Roses":
    price = 5
    total_sum = price * number
    if number > 80:
        total_sum = (price * number)* 0.9
elif type_flowers == "Dahlias":
    price = 3.80
    total_sum = price * number
    if number > 90:
        total_sum = (price * number) * 0.85
elif type_flowers == "Tulips":
    price = 2.80
    total_sum = price * number
    if number > 80:
        total_sum = (price * number) * 0.85
elif type_flowers == "Narcissus":
    price = 3
    total_sum = price * number
    if number < 120:
        total_sum = (price * number) * 1.15
elif type_flowers == "Gladiolus":
    price = 2.50
    total_sum = price * number
    if number < 80:
        total_sum = (price * number) * 1.2
if budget >= total_sum:
    print(f"Hey, you have a great garden with {number} {type_flowers} and {budget - total_sum:.2f} leva left.")
elif budget < total_sum:
    print(f"Not enough money, you need {fabs(total_sum - budget):.2f} leva more.")
