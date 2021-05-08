bitcoin = int(input()) * 1168
uan = float(input())
comission = float(input())

u_to_dol = uan * 0.15
dol_to_lv = u_to_dol * 1.76

result = bitcoin + dol_to_lv
result1 = result - (result * comission / 100)
print(f"{result1 / 1.95:.2f}")
