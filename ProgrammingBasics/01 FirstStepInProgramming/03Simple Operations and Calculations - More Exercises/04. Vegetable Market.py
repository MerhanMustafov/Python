price_kg_vegetables = float(input())
price_kg_fruits = float(input())
kg_vegetables = float(input())
kg_fruits = float(input())

totall_vegetable_price = price_kg_vegetables * kg_vegetables
totall_fruits_price = price_kg_fruits * kg_fruits

totall = (totall_vegetable_price + totall_fruits_price) / 1.94
print(f'{totall:.2f}')
