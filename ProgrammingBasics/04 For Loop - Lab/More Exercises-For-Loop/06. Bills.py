n = int(input())
total_electricity = 0
water = 20 * n
net = 15 * n
others = 0
for i in range(1, n +1):
    electricity = float(input())
    total_electricity += electricity
    others += (electricity + 20 + 15)*1.2
average = (total_electricity + water + net + others) / n
print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {net:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {average:.2f} lv')



# months = int(input())
# electricity = 0
# water = 20
# net = 15
# sum_others = 0
#
#
# for i in range (1, months + 1):
#     price = float(input())
#     electricity += price
#
#     sum_others += (price + water +net)*1.2
#
# water *= months
# net *= months
# average = (electricity + water + net + sum_others) / months
# print(f"Electricity: {electricity:.2f} lv")
# print(f"Water: {water:.2f} lv")
# print(f"Internet: {net:.2f} lv")
# print(f"Other: {sum_others:.2f} lv")
# print(f"Average: {average:.2f} lv")
#
#
