# •	При 100 лв. или по-малко – някъде в България:
# o	Лято – 30% от бюджета;
# o	Зима – 70% от бюджета.
# •	При 1000 лв. или по малко – някъде на Балканите:
# o	Лято – 40% от бюджета;
# o	Зима – 80% от бюджета.
# •	При повече от 1000 лв. – някъде из Европа:
# o	При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета

budget = float(input())
season = input()
price = 0
destination = ""
type_vacation = ""
if season == "summer":
    type_vacation = "Camp"
    if 0 < budget <= 100:#BG
        destination = "Bulgaria"
        price = budget * 0.30
    elif 100 < budget <= 1000:#BALKANI
        destination = "Balkans"
        price = budget * 0.40
    elif budget > 1000:#EU
        type_vacation = "Hotel"
        destination = "Europe"
        price = budget * 0.9


elif season == "winter":
    type_vacation = "Hotel"
    if 0 < budget <= 100:#BG
        destination = "Bulgaria"
        price = budget * 0.7
    elif 100 < budget <= 1000:#BALKANI
        destination = "Balkans"
        price = budget * 0.8
    elif budget > 1000:#EU
        destination = "Europe"
        price = budget * 0.9
print(f"Somewhere in {destination}")
print(f"{type_vacation} - {price:.2f}")