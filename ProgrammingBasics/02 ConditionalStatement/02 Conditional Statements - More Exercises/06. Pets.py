from math import floor
from math import fabs
from math import ceil

days = int(input())
left_food = int(input())
food_for_dog_kg = float(input())* days
food_for_cat_kg = float(input())* days
food_for_turtle_gr = float(input())* days / 1000
totall = food_for_dog_kg + food_for_cat_kg + food_for_turtle_gr
if totall<= left_food:
    print(f'{floor(fabs(totall - left_food))} kilos of food left.')
elif left_food < totall:
    print(f'{ceil(fabs(totall - left_food))} more kilos of food are needed.')
