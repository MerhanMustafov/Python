from collections import deque
total_food_quantity = int(input())
total_orders = deque([int(num) for num in input().split(" ")])

print(max(total_orders))

while total_food_quantity >= 0 and total_orders:
    if not total_food_quantity - total_orders[0] < 0:
        total_food_quantity -= total_orders.popleft()
    else:
        break
if not total_orders:
    print(f"Orders complete")
else:
    left = [str(el) for el in total_orders]
    print(f"Orders left: {' '.join(left)}")



