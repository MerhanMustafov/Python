# •	На първия ред са необходимите часовете – цяло число в интервала [0 ... 200 000]
# •	На втория ред са дните, с които фирмата разполага – цяло число в интервала [0 ... 20 000]
# •	На третия ред е броят на служителите, работещи извънредно – цяло число в интервала [0 ... 200]
from math import floor
from math import fabs
needed_hours = int(input())
days_available = int(input())
overtime_workers = int(input())

percent_for_education = days_available * 0.9 * 8
overtime = overtime_workers * (days_available * 2)
totall_hours = floor(percent_for_education + overtime)
if totall_hours >= needed_hours:
    print(f'Yes!{totall_hours - needed_hours} hours left.')
elif totall_hours < needed_hours:
    hours_needed = (totall_hours - needed_hours)
    print(f'Not enough time!{floor(fabs(hours_needed))} hours needed.')


