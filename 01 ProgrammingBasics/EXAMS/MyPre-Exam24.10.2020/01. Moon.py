# •	На първия ред - средната скорост на движение - реално число в интервала [1000.00... 30000.00]
# •	На втория ред - литри гориво нужни за 100 км - реално число в интервала [1.00…20.00]
import math
average_speed = float(input())
fuel_liter_for_100 = float(input())
total_legth = 384400 * 2
time_go_back = math.ceil(total_legth / average_speed)
total_time = time_go_back + 3
needed_fuel = (fuel_liter_for_100 * total_legth)/100
print(total_time)
print(round(needed_fuel))