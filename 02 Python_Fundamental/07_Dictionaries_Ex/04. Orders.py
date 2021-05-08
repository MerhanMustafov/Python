products = {}
command = input()

while not command == 'buy':
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in products:
        products[product] = {'price': price, 'quantity': quantity}
    else:
        products[product]['price'] = price
        products[product]['quantity'] += quantity

    command = input()
for product, price_quantity_date in products.items():
    total_price = price_quantity_date['price'] * price_quantity_date['quantity']
    print(f"{product} -> {total_price:.2f}")