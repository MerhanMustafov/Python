day = int(input())
room = input()
rate = input()

nights = day - 1
if room == "room for one person":
    nights *= 18
elif room == "apartment":
    nights *= 25
    if day < 10:
        nights = nights - ( nights * 0.3)
    elif 10 <= day <= 15:
        nights = nights - ( nights * 0.35)
    elif day > 15:
        nights = nights - ( nights * 0.5)
elif room == "president apartment":
    nights *= 35
    if day < 10:
        nights = nights - ( nights * 0.1)
    elif 10 <= day <= 15:
        nights = nights - ( nights * 0.15)
    elif day > 15:
        nights = nights - ( nights * 0.2)
if rate == 'positive':
    nights = nights + (nights * 0.25)
elif rate == 'negative':
    nights = nights - (nights * 0.1)
print(f'{nights:.2f}')