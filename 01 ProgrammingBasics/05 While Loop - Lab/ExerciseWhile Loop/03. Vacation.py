needed_money_for_trip = float(input())
available_money = float(input())
days = 0
spend_days = 0


while available_money < needed_money_for_trip and spend_days < 5:
    command = input()
    number = float(input())
    days += 1
    if command == 'save':
        available_money += number
        spend_days = 0
    elif command == 'spend':
        available_money -= number
        spend_days += 1
        if available_money < 0:
            available_money = 0
if available_money >= needed_money_for_trip:
    print(f"You saved the money for {days} days.")
if spend_days == 5:
    print("You can't save the money.")
    print(f"{days}")

# needed_money = float(input())
# money_in_hand = float(input())
# spending_days = 0
# total_days = 0
# while True:
#     action = input()
#     current_sum = float(input())
#     total_days += 1
#     if action == "spend":
#         money_in_hand -= current_sum
#         if money_in_hand < 0:
#             money_in_hand = 0
#         spending_days +=1
#         if spending_days == 5:
#             break
#     elif action == "save":
#         money_in_hand += current_sum
#         if money_in_hand >= needed_money:
#             break
#         spending_days = 0
#
# if money_in_hand >= needed_money:
#     print(f"You saved the money for {total_days} days.")
# else:
#     print("You can't save the money.")
#     print(total_days)