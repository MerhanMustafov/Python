x = float(input())
y = float(input())
h = float(input())

stranichna_stena = x * y
prozorec = 1.5 * 1.5
devete_straniOBSHTo = (stranichna_stena * 2) - (prozorec * 2)
vrata_vxod = 1.2 * 2
zadna_stena = x * x
predna_I_zadna_obshto = 2 * zadna_stena - vrata_vxod

result = devete_straniOBSHTo + predna_I_zadna_obshto
green_paint = result / 3.4

pokriv = 2 * (x * y)
dvata_triugalnika = 2 * (x * h / 2)

reult_obshto = pokriv + dvata_triugalnika
red_paint = reult_obshto / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
