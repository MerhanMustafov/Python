years = int(input())
loundry_price = float(input())

toy = int(input())
current_sum = 0
total_sum = 0
total_toy = 0
brother = 0
for i in range(1, years +1):
    if i == 1:
        total_toy += toy
    elif i % 2 == 0:
        current_sum += 10
        total_sum += current_sum
        brother += 1
    else:
        total_toy += toy
total = (total_toy + total_sum) - brother
if total >= loundry_price:
    print(f'Yes! {total - loundry_price:.2f}')
else:
    print(f'No! {abs(total - loundry_price):.2f}')



# age = int(input())
# washing_machine_price = float(input())
# price_per_one_toy = int(input())
# birthday_price_money = 0
# saved_total_money = 0
#
# number_of_toys = 0
#
# for ages_of_lili in range (1, age + 1):
#     if ages_of_lili % 2 == 0:
#         birthday_price_money += 10
#         saved_total_money += birthday_price_money - 1
#
#     else:
#         number_of_toys += 1
# money_from_toys = number_of_toys * price_per_one_toy
# saved_total_money += money_from_toys
# difference = abs(saved_total_money - washing_machine_price)
# if saved_total_money >= washing_machine_price:
#     print(f"Yes! {difference:.2f}")
# else:
#     print(f"No! {abs(difference):.2f}")
