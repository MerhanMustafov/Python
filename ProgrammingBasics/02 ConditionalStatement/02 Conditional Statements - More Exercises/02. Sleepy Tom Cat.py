from math import fabs
from math import floor
days_off = int(input())
norm = 30000
work_days = 365 - days_off
real_time_for_play = (work_days * 63) + (days_off * 127)
conclusion_in_hours = round(fabs(norm - real_time_for_play) // 60, 2)
conclusion_in_minutes = round(fabs(norm - real_time_for_play) % 60, 2)
if norm < real_time_for_play:
    print('Tom will run away')
    print(f'{floor(conclusion_in_hours)} hours and {floor(conclusion_in_minutes)} minutes more for play')
elif norm > real_time_for_play:
    print('Tom sleeps well')
    print(f'{floor(conclusion_in_hours)} hours and {floor(conclusion_in_minutes)} minutes less for play')
