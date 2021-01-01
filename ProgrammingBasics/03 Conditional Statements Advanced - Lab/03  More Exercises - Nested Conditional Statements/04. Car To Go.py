budget = float(input())
season = input()
class_type = ""
type_of_car = ""
price = 0
if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        type_of_car = "Jeep"
        price = budget * 0.65

elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        type_of_car = "Jeep"
        price = budget * 0.80

elif budget > 500:
    class_type = "Luxury class"
    if season == "Summer" or season == "Winter":
        type_of_car = "Jeep"
        price = budget * 0.9

print(class_type)
print(f"{type_of_car} - {price:.2f}")
