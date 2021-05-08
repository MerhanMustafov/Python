n = int(input())
day_or_night = str(input())
if n < 20:
    taxi = 0.70
    taxi_day = (n * 0.79) + taxi
    taxi_night = (n * 0.9) + taxi
    if day_or_night == 'day':
        print(f'{(taxi_day):.2f}')
    elif day_or_night == 'night':
        print(f'{(taxi_night):.2f}')
elif n >= 20 and n < 100:
    bus_day = n * 0.09
    bus_night = n * 0.09
    if day_or_night == 'day':
        print(f'{(bus_day):.2f}')
    elif day_or_night == 'night':
        print(f'{(bus_night):.2f}')
elif n >= 100:
    train_day = n * 0.06
    train_night = n * 0.06
    if day_or_night == 'day':
        print(f'{(train_day):.2f}')
    elif day_or_night == 'night':
        print(f'{(train_night):.2f}')
