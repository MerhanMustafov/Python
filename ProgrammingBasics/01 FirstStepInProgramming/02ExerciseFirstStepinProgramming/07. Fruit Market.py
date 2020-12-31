strawberries_price = float(input())

bananas_quantity_kg = float(input())
oranges_quantity_kg = float(input())
raspberries_quantity_kg = float(input())
strawberries_quantity_lg = float(input())


raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.4)
bananas_price = raspberries_price - (raspberries_price * 0.8)

price_raspberries = raspberries_price * raspberries_quantity_kg
price_oranges = oranges_price * oranges_quantity_kg
price_bananas = bananas_price * bananas_quantity_kg
price_strawberries = strawberries_price * strawberries_quantity_lg

result = price_bananas + price_oranges+ price_raspberries + price_strawberries
print(result)
