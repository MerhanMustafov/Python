days_pirating_last = int(input())
plunder_for_day = int(input())

expected_plunder_end = float(input())

total = 0

for day in range(days_pirating_last):
    day = day+1
    total += plunder_for_day


    if day % 3 == 0:
        total += (plunder_for_day * 0.5)
    if day % 5 == 0:
        total  *= 0.7

if float(total) >= expected_plunder_end:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    percentage = (total / expected_plunder_end) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")