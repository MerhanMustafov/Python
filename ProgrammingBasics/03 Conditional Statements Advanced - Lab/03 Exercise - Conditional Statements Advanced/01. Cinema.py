screen_type = input()
rows = int(input())
columns = int(input())
income = 0

if screen_type == 'Premiere':
    income = 12
elif screen_type == 'Normal':
    income = 7.5
elif screen_type == 'Discount':
    income = 5
print(f'{(rows * columns) * income:.2f} leva')
