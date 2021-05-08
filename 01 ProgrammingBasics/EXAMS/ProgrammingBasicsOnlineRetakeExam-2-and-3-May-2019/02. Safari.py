# •	Цената на един литър гориво е 2.10 лв.
# •	Цената за екскурзовод е 100лв.
# •	В зависимост от деня има отстъпки от общата цена - за събота 10%, а за неделя 20%
# •	Бюджет – реално число в интервала [0.00… 10000.00]
# •	Колко литра гориво ще са им нужни – реално число в интервала [1.00… 50.00]
# •	Ден от седмицата – текст с възможности "Saturday" и "Sunday"

from math import fabs
price_fuel = 2.1
gueid = 100

budget = float(input())
litra_fuel = float(input())
day = input()

fuel = price_fuel * litra_fuel
total = fuel + gueid

if day == "Saturday":
    total *= 0.9
elif day == "Sunday":
    total *= 0.8
tatal1 = fabs(budget - total)
if budget >= total:
    print(f"Safari time! Money left: {tatal1:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {tatal1:.2f} lv.")
