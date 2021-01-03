size_eggs = input()
color_eggs = input()
number_batch = int(input())#партида

price_per_one_batch = 0
if size_eggs == "Large":
    if color_eggs == "Red":
        price_per_one_batch = 16
    elif color_eggs == "Green":
        price_per_one_batch = 12
    elif color_eggs == "Yellow":
        price_per_one_batch = 9
elif size_eggs == "Medium":
    if color_eggs == "Red":
        price_per_one_batch = 13
    elif color_eggs == "Green":
        price_per_one_batch = 9
    elif color_eggs == "Yellow":
        price_per_one_batch = 7
elif size_eggs == "Small":
    if color_eggs == "Red":
        price_per_one_batch = 9
    elif color_eggs == "Green":
        price_per_one_batch = 8
    elif color_eggs == "Yellow":
        price_per_one_batch = 5
# С 35% от крайната цена ще бъдат покрити производствени разходи.
pure_final_sum = (price_per_one_batch * number_batch) * 0.65
print(f"{pure_final_sum:.2f} leva.")




