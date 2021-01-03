# •	Името на футболния отбор, за който водим статистика - текст
# •	Броя изиграни срещи през настоящия сезон - цяло число в интервала [0… 100]
#  За всяка изиграна среща се прочита отделен ред:
# o	Резултатът от изиграната среща в един от горепосочените формати – символ с възможности 'W', 'D' и 'L'
team = input()
number_maches = int(input())
w = 0
d = 0
l = 0
ponts = 0
for mach in range(1, number_maches + 1):
    result = input()
    if result == 'W':
        w += 1
        ponts += 3
    elif result == 'D':
        d += 1
        ponts += 1
    elif result == 'L':
        l += 1
        ponts += 0
if number_maches <= 0:
    print(f"{team} hasn't played any games during this season.")
elif number_maches > 0:
    print(f"{team} has won {ponts} points during this season.")
    print("Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {w / number_maches * 100:.2f}%")