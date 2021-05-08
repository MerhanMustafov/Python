# •	Брой дни – цяло число в интервала [1 … 5]
# •	Брой часове за всеки един от дните - цяло число в интервала [1 … 24]
number_days = int(input())
number_hours = int(input())
parking_tax = 0
total = 0

for each_day in range(1, number_days + 1):
    total_per_day = 0
    current_day = each_day
    for each_hour in range (1, number_hours + 1):
        if each_day % 2 == 0 and each_hour % 2 != 0:
            parking_tax = 2.5
        elif each_day % 2 != 0 and each_hour % 2 == 0:
            parking_tax = 1.25
        else:
            parking_tax = 1
        total_per_day += parking_tax
        total += parking_tax
    print(f"Day: {current_day} - {total_per_day:.2f} leva")
print(f"Total: {total:.2f} leva")
