from collections import deque
def int_to_str(lst):
    return [str(n) for n in lst]

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])


milkshakes = 0
while chocolates and cups_of_milk:
    if chocolates[-1] <= 0 or cups_of_milk[0] <= 0:
        if cups_of_milk[0] <= 0:
            cups_of_milk.popleft()
        if chocolates[-1] <= 0:
            chocolates.pop()


    else:
        if chocolates[-1] == cups_of_milk[0]:
            milkshakes += 1
            chocolates.pop(), cups_of_milk.popleft()

        else:
            chocolates[-1] -= 5
            cups_of_milk.append(cups_of_milk.popleft())
        if milkshakes == 5:
            break
        if not chocolates or not cups_of_milk:
            break

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
elif milkshakes < 5:
    print(f"Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(int_to_str(chocolates))}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(int_to_str(cups_of_milk))}")
else:
    print("Milk: empty")
