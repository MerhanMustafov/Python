from math import fabs
price_trip = float(input())
puz= int(input())
talkingDolls = int(input())
teddy_bear = int(input())
minions = int(input())
trucks = int(input())
totall_cost = (puz * 2.60) + (talkingDolls * 3) + (teddy_bear * 4.10) + (minions * 8.20) + (trucks * 2)
number_toys = puz + talkingDolls + teddy_bear + minions + trucks
discount = 0.75
rent = 0.9


if number_toys >= 50:
    totall_cost *= discount
totall_cost *= rent
if totall_cost >= price_trip:
    print(f"Yes! {fabs(totall_cost - price_trip):.2f} lv left.")
else:
     print(f"Not enough money! {fabs(price_trip - totall_cost):.2f} lv needed.")

