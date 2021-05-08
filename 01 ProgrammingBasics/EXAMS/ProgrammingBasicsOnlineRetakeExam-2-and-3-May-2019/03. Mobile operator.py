# 1.	Срок на договор – текст – "one", или "two"
# 2.	Тип на договор – текст – "Small",  "Middle", "Large"или "ExtraLarge"
# 3.	Добавен мобилен интернет – текст – "yes" или "no"
# 4.	Брой месеци за плащане - цяло число в интервала [1 … 24]

deadline = input()
type = input()
internet = input()
months = int(input())
price = 0
two = False

if deadline == "one":
    if type == "Small":
        price = 9.98
    elif type == "Middle":
        price = 18.99
    elif type == "Large":
        price = 25.98
    elif type == "ExtraLarge":
        price = 35.99

elif deadline == "two":
    two = True
    if type == "Small":
        price = 8.58
    elif type == "Middle":
        price = 17.09
    elif type == "Large":
        price = 23.59
    elif type == "ExtraLarge":
        price = 31.79

if internet == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85
elif internet == "no":
    price = price
if two == True:
    price *= 0.9625
price *= months
print(f"{price:.2f} lv.")