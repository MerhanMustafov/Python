stadium_capacity = int(input())
number = int(input())

sectorA = 0
sectorB = 0
sectorV = 0
sectorG = 0


for letter in range (1, number + 1):
    text = input()
    if text == 'A':
        sectorA += 1
    if text == 'B':
        sectorB += 1
    if text == 'V':
        sectorV += 1
    if text == 'G':
        sectorG += 1
print(f'{sectorA / number * 100:.2f}%')
print(f'{sectorB / number * 100:.2f}%')
print(f'{sectorV / number * 100:.2f}%')
print(f'{sectorG / number * 100:.2f}%')
print(f'{number / stadium_capacity * 100:.2f}%')