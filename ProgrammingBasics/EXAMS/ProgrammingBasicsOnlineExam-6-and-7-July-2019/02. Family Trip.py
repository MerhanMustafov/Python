# •	Бюджетът, с който разполагат – реално число в интервала [1.00 … 10000.00]
# •	Брой нощувки – цяло число в интервала [0 … 1000]
# •	Цена за нощувка – реално число в интервала [1.00 … 500.00]
# •	Процент за допълнителни разходи – цяло число в интервала [0 … 100]

budget = float(input())
nights = int(input())
price_per_night = float(input())
perset_for_further_outcome = int(input())

if nights > 7:
    price_per_night *= 0.95
price_for_allNights = price_per_night * nights
price_plus_further = (budget * perset_for_further_outcome/100)
price = price_for_allNights + price_plus_further
if price <= budget:
    left_after = abs(budget - price)
    print(f"Ivanovi will be left with {left_after:.2f} leva after vacation.")
else:
    needed_more = abs(budget - price)
    print(f"{needed_more:.2f} leva needed.")