def int_to_str(list_of_sth):
    return [str(el) for el in list_of_sth]

from collections import deque
pizza_orders = deque([int(el) for el in input().split(", ")])
employee_capasity = [int(el) for el in input().split(", ")]


total_pizza_made = 0
while pizza_orders and employee_capasity:

    if pizza_orders[0] > 10 or pizza_orders[0] <= 0:
        pizza_orders.popleft()
    else:
        if pizza_orders[0] <= employee_capasity[-1]:
            total_pizza_made += pizza_orders.popleft()
            employee_capasity.pop()
        else:
            total_pizza_made += employee_capasity[-1]
            pizza_orders[0] -= employee_capasity.pop()

if employee_capasity:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_made}")
    print(f"Employees: {', '.join(int_to_str(employee_capasity))}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(int_to_str(pizza_orders))}")

# https://pastebin.com/yg5v7nTP