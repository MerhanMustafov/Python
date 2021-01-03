# •	Първи ред - напитка - текст с възможности"Espresso", "Cappuccino" или "Tea"
# •	Втори ред - захар - текст  с възможности "Without", "Normal" или "Extra"
# •	Трети ред - брой напитки - цяло число в интервала [1… 50]

beverage = input()
shugar = input()
number_beverages = int(input())
price = 0
without_shugar = False
over5 = False
if beverage == "Espresso":
    if shugar == "Without":
        price = 0.9
        without_shugar = True
    elif shugar == "Normal":
        price = 1
    elif shugar == "Extra":
        price = 1.2
    if number_beverages >= 5:
        over5 = True
elif beverage == "Cappuccino":
    if shugar == "Without":
        price = 1
        without_shugar = True
    elif shugar == "Normal":
        price = 1.2
    elif shugar == "Extra":
        price = 1.6

elif beverage == "Tea":
    if shugar == "Without":
        price = 0.5
        without_shugar = True
    elif shugar == "Normal":
        price = 0.6
    elif shugar == "Extra":
        price = 0.7

total = price * number_beverages
if without_shugar:
    total *= 0.65
if over5:
    total *= 0.75
if total > 15:
    total *= 0.8
print(f"You bought {number_beverages} cups of {beverage} for {total:.2f} lv.")
