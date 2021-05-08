# 1.	Рекордът в секунди – реално число в интервала [0.00 … 100000.00]
# 2.	Разстоянието в метри – реално число в интервала [0.00 … 100000.00]
# 3.	Времето в секунди, за което изкачва 1 м. – реално число в интервала [0.00 … 1000.00]
from math import floor
from math import fabs

record = float(input())
length_m = float(input())
time_in_seconds = float(input())

need_to_climd_sec = length_m * time_in_seconds
slow_down = floor(length_m / 50) * 30
total_time = need_to_climd_sec + slow_down
if record <= total_time:
    total_time -= record
    print(f"No! He was {fabs(total_time):.2f} seconds slower.")
elif record > total_time:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
