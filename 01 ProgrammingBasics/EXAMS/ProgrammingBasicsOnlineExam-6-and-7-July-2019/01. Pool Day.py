# 1.	Първи ред – брой на хората. Цяло число в интервала [1…100]
# 2.	Втори ред – такса вход. Реално число в интервала [0.00…50.00]
# 3.	Трети ред – цена един за шезлонг. Реално число в интервала [0.00…50.00]
# 4.	Четвърти ред – цена за един чадър. Реално число в интервала [0.00...50.00]
from math import ceil
number_people = int(input())
entry_tax = float(input())
sun_bed_price = float(input())
umbrela_price = float(input())

total_entry_price = number_people * entry_tax
tsun_bed = ceil(number_people * 0.75)
total_sun_bed = tsun_bed * sun_bed_price
tumbrella = ceil(number_people * 0.5)
total_umbrellas = tumbrella * umbrela_price
total = total_entry_price + total_sun_bed + total_umbrellas
print(f"{total:.2f} lv." )