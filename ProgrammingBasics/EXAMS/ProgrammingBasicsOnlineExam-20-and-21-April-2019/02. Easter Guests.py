from math import ceil
number_of_guests = int(input())
budget = int(input())

number_easter_bread = ceil(number_of_guests / 3)
number_eggs = number_of_guests * 2

price_easter_bread = number_easter_bread * 4
price_eggs = number_eggs * 0.45
total_sum = price_easter_bread + price_eggs
if budget >= total_sum:
    print(f"Lyubo bought {number_easter_bread} Easter bread and {number_eggs} eggs.")
    print(f"He has {budget - total_sum:.2f} lv. left.")
elif budget < total_sum:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {total_sum - budget:.2f} lv. more.")