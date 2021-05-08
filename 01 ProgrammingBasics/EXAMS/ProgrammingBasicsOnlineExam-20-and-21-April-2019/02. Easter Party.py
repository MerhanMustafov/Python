# 1.	Брой гости – цяло число в интервала [1...99]
# 2.	Цена на куверт за един човек – реално число в интервала [0.00 … 99.00]
# 3.	Бюджетът на Деси  – реално число в интервала [0.00 … 9999.00]
guests = int(input())
kuvert = float(input())
budget = float(input())

cake = budget * 0.1
if 10 <= guests <= 15:
    kuvert *= 0.85
elif 15 < guests <= 20:
    kuvert *= 0.8
elif guests > 20:
    kuvert *= 0.75
needed_sum = (guests * kuvert) + cake
if budget < needed_sum:
    print(f"No party! {abs(budget - needed_sum):.2f} leva needed.")
elif budget >= needed_sum:
    print(f"It is party time! {abs(budget - needed_sum):.2f} leva left.")
