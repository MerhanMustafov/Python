# •	 Броят на козунаците – цяло число в интервала [1 ... 100]
import sys
import math
eater_bread = int(input())
max_flour = -sys.maxsize
max_sugar = -sys.maxsize
total_sugar = 0
total_flour = 0
for current_easter_bread in range(1, eater_bread+1):
    sugar = int(input())
    total_sugar += sugar
    if sugar > max_sugar:
        max_sugar = sugar
    flour = int(input())
    total_flour += flour
    if flour > max_flour:
        max_flour = flour
print(f"Sugar: {math.ceil(total_sugar / 950)}")
print(f"Flour: {math.ceil(total_flour / 750)}")
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')