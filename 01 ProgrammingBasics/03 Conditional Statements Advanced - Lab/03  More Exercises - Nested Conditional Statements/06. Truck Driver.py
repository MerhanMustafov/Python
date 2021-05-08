# •	Първи ред – Сезон – текст "Spring", "Summer", "Autumn" или "Winter"
# •	Втори ред –  Километри на месец – реално число в интервала [10.00...20000.00]
season = input()
km_per_month = float(input())
price_per_km = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.9
    elif season == "Winter":
        price_per_km = 1.05

elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.10
    elif season == "Winter":
        price_per_km = 1.25

elif 10000 < km_per_month <= 20000:
    if season == "Spring" or season == "Autumn" or season == "Winter" or season == "Summer":
        price_per_km = 1.45

salary = ((km_per_month * price_per_km) * 4) * 0.9
print(f"{salary:.2f}")

