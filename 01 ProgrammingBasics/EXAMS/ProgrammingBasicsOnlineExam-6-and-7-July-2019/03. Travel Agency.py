# 1.	Име на града - текст с възможности ("Bansko",  "Borovets", "Varna" или "Burgas")
# 2.	Вид на пакета - текст с възможности ("noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# 3.	Притежание на VIP отстъпка - текст с възможности  "yes" или "no"
# 4.	Дни за престой - цяло число в интервала [1 … 10000]
import sys
city_name = input()
type_pack = input()
vip = input()
days_stay = int(input())
days = False
price = 0
correct = False
if city_name == "Bansko" or city_name == "Borovets":
    if type_pack == "noEquipment":
        price = 80
        if vip == "no":
            price = price
        elif vip == "yes":
            price *= 0.95
    elif type_pack == "withEquipment":
        price = 100
        if vip == "yes":
            price *= 0.9
        elif vip == "no":
            price = price

    correct = True
elif city_name == "Varna" or city_name == "Burgas":
    if type_pack == "noBreakfast":
        price = 100
        if vip == "yes":
            price *= 0.93
        if vip == "no":
            price = price
    elif type_pack == "withBreakfast":
        price = 130
        if vip == "yes":
            price *= 0.88
        if vip == "no":
            price = price

    correct = True
if days_stay < 1:
    print("Days must be positive number!")
    sys.exit(0)
if not correct:
    print("Invalid input!")
    sys.exit(0)


if days_stay <= 7:
    total = price * days_stay
    print(f"The price is {total:.2f}lv! Have a nice time!")
    sys.exit(0)
if days_stay > 7:
    total = (price * days_stay) - price
    print(f"The price is {total:.2f}lv! Have a nice time!")
    sys.exit(0)
