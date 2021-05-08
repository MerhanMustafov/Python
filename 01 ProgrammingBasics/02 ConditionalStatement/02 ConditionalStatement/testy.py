price_trip = float(input())
puzzel = int(input())
talkingDolls = int(input())
teddy_bear = int(input())
minions = int(input())
trucks = int(input())
from  math import fabs
totall_cost = (puzzel* 2.60) + (talkingDolls * 3) + (teddy_bear * 4.10) + (minions * 8.20) + (trucks * 2)
nuber_toys = puzzel + talkingDolls + teddy_bear + minions + trucks
totall_cost *= 0.9
if nuber_toys >=50:
    totall_cost *=0.75

if totall_cost >= price_trip:
    print(f"Yes! {(totall_cost -price_trip):.2f} lv left.")
else:
    print(f"Not enough money! {(price_trip-totall_cost):.2f} lv needed.")