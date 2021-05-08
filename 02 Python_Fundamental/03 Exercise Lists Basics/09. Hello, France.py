MAX_PRICE_CLOTHES = 50.00
MAX_PRICE_SHOES = 35.00
MAX_PRICE_ACCESSORIES = 20.50

items = input().split("|")
budget = float(input())

increased_price = []
profit = []

for index in items:
    type_item, price_item = index.split("->")
    price_item = float(price_item)
    if type_item == "Clothes" and price_item > MAX_PRICE_CLOTHES:
        continue
    elif type_item == "Shoes" and price_item > MAX_PRICE_SHOES:
        continue
    elif type_item == "Accessories" and price_item > MAX_PRICE_ACCESSORIES:
        continue

    if budget >= price_item:
        budget -= price_item
        increase = price_item * 0.4 + price_item
        profit.append(increase - price_item)
        increased_price.append(increase)
for n in increased_price:
   print(f"{n:.2f}", end=" ")

print(f"\nProfit: {sum(profit):.2f}")
if budget + sum(increased_price) <= 150:
    print("Time to go.")
else:
    print("Hello, France!")