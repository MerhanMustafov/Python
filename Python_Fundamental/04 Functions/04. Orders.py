def calc_price(item, quantity):
    result = 0
    if item == "coffee":
        result = quantity * 1.50
    elif item == "water":
        result = quantity * 1.00
    elif item == "coke":
        result = quantity * 1.40
    elif item == "snacks":
        result = quantity * 2.00
    return result

item = input()
quantity = float(input())
print(f"{calc_price(item, quantity):.2f}")
