# •	Първият ред – отбор – текст с възможности: "Argentina", "Brazil", "Croatia", "Denmark"
# •	Вторият ред – вид сувенири – текст с възможности: "flags", "caps", "posters", "stickers"
# •	Третият ред – брой закупени сувенири – цяло число в интервала [1…200]
import sys
team = input()
suvenir = input()
bought_suvenirs = int(input())
price = 0

if team == 'Argentina':
    if suvenir == 'flags':
        price += bought_suvenirs * 3.25
    elif suvenir == 'caps':
        price += bought_suvenirs * 7.20
    elif suvenir == 'posters':
        price += bought_suvenirs * 5.10
    elif suvenir == 'stickers':
        price += bought_suvenirs * 1.25
    else:
        print("Invalid stock!")
        sys.exit(0)
elif team == 'Brazil':
    if suvenir == 'flags':
        price += bought_suvenirs *4.20
    elif suvenir == 'caps':
        price += bought_suvenirs *8.5
    elif suvenir == 'posters':
        price += bought_suvenirs *5.35
    elif suvenir == 'stickers':
        price += bought_suvenirs *1.2
    else:
        print("Invalid stock!")
        sys.exit(0)
elif team == 'Croatia':
    if suvenir == 'flags':
        price += bought_suvenirs *2.75
    elif suvenir == 'caps':
        price += bought_suvenirs *6.9
    elif suvenir == 'posters':
        price += bought_suvenirs *4.95
    elif suvenir == 'stickers':
        price += bought_suvenirs *1.1
    else:
        print("Invalid stock!")
        sys.exit(0)
elif team == 'Denmark':
    if suvenir == 'flags':
        price += bought_suvenirs *3.10
    elif suvenir == 'caps':
        price += bought_suvenirs *6.5
    elif suvenir == 'posters':
        price += bought_suvenirs *4.8
    elif suvenir == 'stickers':
        price += bought_suvenirs *0.9
    else:
        print("Invalid stock!")
        sys.exit(0)
else:
    print("Invalid country!")
    sys.exit(0)
print(f'Pepi bought {bought_suvenirs} {suvenir} of {team} for {price:.2f} lv.')