money_available = float(input())
gender = input()
age = int(input())
sport_type = input()
card_price = 0

if gender == "m":
    if sport_type == "Gym":
        card_price = 42
    elif sport_type == "Boxing":
        card_price = 41
    elif sport_type == "Yoga":
        card_price = 45
    elif sport_type == "Zumba":
        card_price = 34
    elif sport_type == "Dances":
        card_price = 51
    elif sport_type == "Pilates":
        card_price = 39
if gender == "f":
    if sport_type == "Gym":
        card_price = 35
    elif sport_type == "Boxing":
        card_price = 37
    elif sport_type == "Yoga":
        card_price = 42
    elif sport_type == "Zumba":
        card_price = 31
    elif sport_type == "Dances":
        card_price = 53
    elif sport_type == "Pilates":
        card_price = 37
if age <= 19:
    card_price *= 0.80
if card_price <= money_available:
    print(f"You purchased a 1 month pass for {sport_type}.")
elif card_price > money_available:
    neede_money = card_price - money_available
    print(f"You don't have enough money! You need ${neede_money:.2f} more.")

