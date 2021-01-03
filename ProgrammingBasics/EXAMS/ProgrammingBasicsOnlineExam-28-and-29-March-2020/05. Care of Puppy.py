bought_kg_food = int(input())
bought_in_gr = bought_kg_food * 1000
total_eaten = 0
command = input()
while command != 'Adopted':
    eat = int(command)
    total_eaten += eat
    command = input()

leftover = abs(bought_in_gr - total_eaten)
if total_eaten <= bought_in_gr:
    print(f"Food is enough! Leftovers: {leftover} grams.")
else:
    print(f"Food is not enough. You need {leftover} grams more." )