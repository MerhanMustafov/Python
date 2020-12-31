from math import fabs

budget = float(input())
stats_number = int(input())
price_for_one_costume = float(input())
decor_price = budget * 0.10
price_costume = stats_number * price_for_one_costume
if stats_number > 150:
    price_costume *= 0.90
total = decor_price + price_costume
total_sum = budget - total

if budget >= total:
    print("Action! ")
    print(f"Wingard starts filming with {fabs(total_sum):.2f} leva left.")
elif budget < total:
    print("Not enough money!")
    print(f"Wingard needs {fabs(total_sum):.2f} leva more.")