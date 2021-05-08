import math
days = int(input())
food_left = int(input())
food_for_dog_day = float(input())
food_for_cat_day = float(input())
food_for_turtle_day = float(input())
food_for_turtle_day /= 1000

needed_food_dog = days * food_for_dog_day
needed_food_cat = days * food_for_cat_day
needed_food_turtle = days * food_for_turtle_day

total_food = needed_food_cat + needed_food_dog + needed_food_turtle

food_rest = food_left - total_food
food_needed = abs(total_food - food_left)

if food_left >= total_food:
    print(f"{math.floor(math.fabs(food_rest))} kilos of food left.")
else:
    print(f"{math.ceil(food_needed)} more kilos of food are needed.")