# 1.	Бюджетът на Петър - реално число в интервала [0.0…100000.0]
# 2.	Броят видеокарти - цяло число в интервала [0…100]
# 3.	Броят процесори - цяло число в интервала [0…100]
# 4.	Броят рам памет - цяло число в интервала [0…100]
budget_pesho = float(input())
num_videocards = int(input())
num_prosessors = int(input())
num_ram = int(input())

total_videocards = num_videocards * 250
total_prossesors = total_videocards * 0.35 * num_prosessors
total_ram = total_videocards * 0.1 * num_ram
total = total_videocards + total_prossesors +total_ram
if num_videocards > num_prosessors:
    total *= 0.85
if budget_pesho >= total:
    left = abs(budget_pesho - total)
    print(f"You have {left:.2f} leva left!")
else:
    needed = abs(budget_pesho - total)
    print(f"Not enough money! You need {needed:.2f} leva more!")

