skuria_priceKG = float(input())
caca_priceKG = float(input())

palamud_KG = float(input())
safrid_KG = float(input())
midi_KG = int(input()) * 7.50

palamud_priceKG = skuria_priceKG + (skuria_priceKG * 0.6)
sum_palamud = palamud_KG * palamud_priceKG
safrid_priceKG = caca_priceKG + (caca_priceKG * 0.8)
sum_safrid = safrid_KG * safrid_priceKG

sum_midi = midi_KG

result = sum_midi + sum_safrid + sum_palamud
import math
print(f'{result:.2f}')
