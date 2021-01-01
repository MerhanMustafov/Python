number_juniors = int(input())
number_seniors = int(input())
type_road = input() #True
total_number_of_participants = number_juniors + number_seniors

price_juniors = 0
price_seniors = 0
if type_road == "trail":
    price_juniors = 5.5
    price_seniors = 7
elif type_road == "cross-country":
    type_road = False
    price_juniors = 8
    price_seniors = 9.5
elif type_road == "downhill":
    price_juniors = 12.25
    price_seniors = 13.75
elif type_road == "road":
    price_juniors = 20
    price_seniors = 21.5

total_sum = (number_juniors * price_juniors) + (number_seniors * price_seniors)
outgo = total_sum * 0.05

money_for_donation = total_sum - outgo
if type_road == False:
    if total_number_of_participants >= 50:
        money_for_donation *= 0.75
print(f"{money_for_donation:.2f}")
