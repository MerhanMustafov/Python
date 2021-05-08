budget = float(input())
enough = True

needed = 0

num_product = 0
total = 0
day = 1
command = input()
while command != 'Stop':
    price_product = float(input())
    if day % 3 == 0:
        price_product *= 0.5
    if price_product > budget:
        enough = False
        needed = abs(budget - price_product)
        break
    budget -= price_product
    num_product += 1
    total += price_product
    day += 1
    command = input()
if enough == False:
    print("You don't have enough money!")
    print(f"You need {needed:.2f} leva!")
else:
    print(f"You bought {num_product} products for {total:.2f} leva.")
