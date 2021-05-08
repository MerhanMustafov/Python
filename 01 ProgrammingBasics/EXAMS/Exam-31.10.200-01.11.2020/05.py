import sys
number_trip_sea = int(input())
number_trip_mountain = int(input())
profit = 0

name_pack = input()
while name_pack != 'Stop':
    if name_pack == 'sea':
        if number_trip_sea == 0:
            name_pack = input()
            continue
        profit += 680
        number_trip_sea -= 1
    elif name_pack == "mountain":
        if number_trip_mountain == 0:
            name_pack = input()
            continue
        profit += 499
        number_trip_mountain -= 1
    if number_trip_sea == 0 and number_trip_mountain == 0:
        print(" Good job! Everything is sold.")
        print(f"Profit: {profit} leva.")
        sys.exit(0)
    name_pack = input()
if name_pack == 'Stop':
    print(f"Profit: {profit} leva.")
