km = float(input())
day_time = str(input())

taxi_start = 0.70
taxi_day = 0.79
taxi_night = 0.90
bus = 0.09
train = 0.06

price_day = km * taxi_day + taxi_start
price_night = km * taxi_night + taxi_start
price_bus = km * bus
price_train = km * train

if km < 20:
    if day_time == "day":
        print(f"{price_day:.2f}")
    elif day_time == "night":
        print(f"{price_night:.2f}")
elif km >= 20 and km < 100:
    if day_time == "day":
        print(f"{price_bus:.2f}")
    elif day_time == "night":
        print(f"{price_bus:.2f}")
elif km >= 100:
    if day_time == "day":
        print(f"{price_train:.2f}")
    elif day_time == "night":
        print(f"{price_train:.2f}")
