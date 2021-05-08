number_of_days = int(input())
total_quantity = float(input())
total_eaten_dog = 0
total_eaten_cat = 0
total_cookie = 0
for days in range (1, number_of_days +1):
    dog = int(input())
    cat = int(input())

    total_eaten_dog += dog
    total_eaten_cat += cat

    total_per_day = dog + cat
    if days % 3 == 0:
        cookie = total_per_day * 0.1
        total_cookie += cookie

hole_eaten = total_eaten_dog + total_eaten_cat
print(f"Total eaten biscuits: {round(total_cookie)}gr.")
print(f"{(hole_eaten / total_quantity) * 100:.2f}% of the food has been eaten.")
print(f"{(total_eaten_dog / hole_eaten) * 100:.2f}% eaten from the dog.")
print(f"{(total_eaten_cat / hole_eaten) * 100:.2f}% eaten from the cat.")
