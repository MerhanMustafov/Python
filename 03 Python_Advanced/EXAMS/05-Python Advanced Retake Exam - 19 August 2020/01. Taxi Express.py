from collections import deque

def int_to_str(customers):
    return [str(n) for n in customers]

customers = deque([int(el) for el in input().split(", ")])
taxis = [int(el) for el in input().split(", ")]
time = 0
while customers and taxis:

    if customers[0] <= taxis[-1]:
        time += customers[0]
        customers.popleft(), taxis.pop()
    else:
        taxis.pop()
if customers:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(int_to_str(customers))}")
else:
    print(f"All customers were driven to their destinations\nTotal time: {time} minutes")



