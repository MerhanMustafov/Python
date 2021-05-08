# •	Брой продадени игри- n - цяло положително число в интервала [1… 100]
# За следващите n реда се чете по един ред:
# o	Име на игра - текст
number_sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for one in range (1, number_sold_games + 1):
    game_name = input()
    if game_name == 'Hearthstone':
        hearthstone += 1
    elif game_name == 'Fornite':
        fornite += 1
    elif game_name == 'Overwatch':
        overwatch += 1
    else:
        others += 1
hearthstone_percent = hearthstone / number_sold_games * 100
fornite_percent = fornite / number_sold_games * 100
overwatch_percent = overwatch / number_sold_games * 100
others_percent = others / number_sold_games * 100

print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")