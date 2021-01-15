budget = float(input())
price_1kg_flour = float(input())

price_egg = price_1kg_flour * 0.75
pricee_1l_milk = price_1kg_flour * 1.25
price_0_250l_milk = pricee_1l_milk/4

total_price_per_cozunac = price_1kg_flour + price_egg + price_0_250l_milk

cozunacs_counter = 0
colored_eggs = 0

while budget > total_price_per_cozunac:
    cozunacs_counter += 1
    colored_eggs += 3
    budget -= total_price_per_cozunac
    if cozunacs_counter % 3 == 0:
        colored_eggs -= (cozunacs_counter - 2)
print(f'You made {cozunacs_counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
budget = float(input())
price_1kg_flour = float(input())

price_egg = price_1kg_flour * 0.75
pricee_1l_milk = price_1kg_flour * 1.25
price_0_250l_milk = pricee_1l_milk/4

total_price_per_cozunac = price_1kg_flour + price_egg + price_0_250l_milk

cozunacs_counter = 0
colored_eggs = 0

while budget > total_price_per_cozunac:
    cozunacs_counter += 1
    colored_eggs += 3
    budget -= total_price_per_cozunac
    if cozunacs_counter % 3 == 0:
        colored_eggs -= (cozunacs_counter - 2)
print(f'You made {cozunacs_counter} cozonacs! Now you have {colored_eggs} eggs and {budget}BGN left.)
