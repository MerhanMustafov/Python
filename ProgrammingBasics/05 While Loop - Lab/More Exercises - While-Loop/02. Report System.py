expected_money = int(input())
time = 0
cash = True
card = True

cash_count = 0
card_count = 0

sum_cash = 0
sum_card = 0
is_enough = False

command = input()
while command != "End":
    product_price = int(command)
    time += 1
    if time % 2 != 0:
        if product_price > 100:
            cash=False
            print("Error in transaction!")
            command = input()
            continue
        cash_count += 1
        sum_cash += product_price
        print("Product sold!")
    elif time % 2 == 0:
        if product_price <= 10:
            card = False
            print("Error in transaction!")
            command = input()
            continue
        card_count += 1
        sum_card += product_price
        print("Product sold!")
    sum = sum_cash + sum_card
    if sum >= expected_money:
        is_enough = True
        break
    command = input()

if is_enough:
    average_cash = sum_cash / cash_count
    average_card = sum_card / card_count
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}" )
elif command == 'End':
    print("Failed to collect required money for charity.")

