# 1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3.	Количество разредител (в литри) - цяло число в интервала [1…30]
# 4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
needed_nylon = int(input())+2
needed_paint_ltr = int(input())*1.1
thinner = int(input())
hours_for_compeleting = int(input())

price_nylon = needed_nylon * 1.5
price_paint = needed_paint_ltr * 14.5
price_thinner = thinner * 5
price_with_bags = price_nylon + price_paint + price_thinner +0.4
for_workars = hours_for_compeleting * (price_with_bags * 0.3)
total = for_workars + price_with_bags
print(f"Total expenses: {total:.2f} lv.")