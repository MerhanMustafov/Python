# •	Брой пилешки менюта – цяло число в интервала [0… 99]
# •	Брой менюта с риба - цяло число в интервала [0… 99]
# •	Брой вегетариански менюта - цяло число в интервала [0… 99]
# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.


num_chicken = int(input())
num_fish = int(input())
num_vegeterian = int(input())
price_chicken = 10.35
price_fish = 12.40
price_vegeterian = 8.15

total_ch = num_chicken * price_chicken
total_fish = num_fish * price_fish
total_vege = num_vegeterian * price_vegeterian

total_price = total_ch + total_fish + total_vege
desert = total_price * 0.2
delivery = 2.5

total = total_price + desert + delivery
print(f"Total: {total:.2f}")

