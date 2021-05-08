from math import fabs

budget = float(input())
broi_statisti = int(input())
cena_obleklo_za_1_statist = float(input())
dekor_za_filma = budget * 0.1
sumata = dekor_za_filma + (broi_statisti * cena_obleklo_za_1_statist)
if broi_statisti > 150:
    cena_obleklo_za_1_statist *= 0.9
    sumata = dekor_za_filma + (broi_statisti * cena_obleklo_za_1_statist)
if sumata > budget:
    print("Not enough money!")
    print(f'Wingard needs {fabs(budget - sumata):.2f} leva more.')
if sumata <= budget:
    print('Action!')
    print(f'Wingard starts filming with {fabs(budget - sumata):.2f} leva left.')
