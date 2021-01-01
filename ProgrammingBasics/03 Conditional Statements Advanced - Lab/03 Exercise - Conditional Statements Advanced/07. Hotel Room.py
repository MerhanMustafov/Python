# •	На първия ред е месецът – May, June, July, August, September или October;
# •	На втория ред е броят на нощувките – цяло число.
month = input()
nights = int(input())
studio_price = 0
apartment_price = 0
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < nights < 14 :
        studio_price *= 0.95
    elif nights > 14:
        studio_price *= 0.7

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price *= 0.8
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
if apartment_price and nights > 14:
    apartment_price *= 0.9
print(f"Apartment: {apartment_price * nights:.2f} lv.")
print(f"Studio: {studio_price * nights:.2f} lv.")

# Решение на някого друг. На този код му даваше 90/100 но аз добавих на if...and (...or...) скоби, защото, когато имаме
# and и or в един if трябва да са разганичени, отделени със скоби
# month = input()
# number_of_nights = int(input())
#
# if month == "May" or month == "October":
#     studio = 50
#     apartment = 65
# elif month == "June" or month == "September":
#     studio = 75.20
#     apartment = 68.70
# elif month == "July" or month == "August":
#     studio = 76
#     apartment = 77
#
# price_for_studio = studio * number_of_nights
# price_for_apartment = apartment * number_of_nights
#
# if 7 < number_of_nights < 14 and (month == "May" or month == "October"):
#     price_for_studio *= 0.95
# elif number_of_nights > 14 and (month == "May" or month == "October"):
#     price_for_studio *= 0.70
# elif number_of_nights > 14 and (month == "June" or month == "September"):
#     price_for_studio *= 0.80
# if number_of_nights > 14:
#     price_for_apartment *= 0.90
#
# print(f"Apartment: {price_for_apartment:.2f} lv.")
# print(f"Studio: {price_for_studio:.2f} lv.")
