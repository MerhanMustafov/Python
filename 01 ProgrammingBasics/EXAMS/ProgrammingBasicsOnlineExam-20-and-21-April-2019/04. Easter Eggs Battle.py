# 1.	Брой яйца, които има първият играч - цяло число в интервала [1 … 99]
# 2.	Брой яйца, които има вторият играч - цяло число в интервала [1 … 99]
player_1 = int(input())
player_2 = int(input())
command = input()
while command != "End of battle":
    if command == "one":
        player_2 -= 1
        if player_2 == 0:
            print(f"Player two is out of eggs. Player one has {player_1} eggs left.")
            break
    elif command == "two":
        player_1 -= 1
        if player_1 == 0:
            print(f"Player one is out of eggs. Player two has {player_2} eggs left.")
            break
    command = input()
if command == "End of battle":
    print(f"Player one has {player_1} eggs left.")
    print(f"Player two has {player_2} eggs left.")