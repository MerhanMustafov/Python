n = int(input())

bus = 0
truck = 0
train = 0

for i in range(1, n + 1):
    tons = int(input())
    if tons <= 3:
        bus += tons
    elif 4 <= tons <= 11:
        truck += tons
    elif tons >= 12:
        train += tons
total_number_cargo = bus + truck + train
avarege_for_tone = (bus * 200 + truck * 175 + train * 120) / total_number_cargo
print(f'{avarege_for_tone:.2f}')
print(f'{bus / total_number_cargo * 100:.2f}%')
print(f'{truck / total_number_cargo * 100:.2f}%')
print(f'{train / total_number_cargo * 100:.2f}%')
