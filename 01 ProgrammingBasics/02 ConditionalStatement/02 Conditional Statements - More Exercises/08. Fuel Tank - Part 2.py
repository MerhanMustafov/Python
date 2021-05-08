fuel = str(input())
fuel_litre = float(input())
club_card = str(input())
price_diesel= 2.33
price_gasoline = 2.22
price_gas = 0.93
total_sum = 0

if club_card == 'Yes':
    price_diesel -= 0.12
    price_gas -= 0.08
    price_gasoline -= 0.18
if fuel == 'Gas':
    total_sum = price_gas * fuel_litre
elif fuel == 'Gasoline':
    total_sum = price_gasoline * fuel_litre
elif fuel == 'Diesel':
    total_sum = price_diesel * fuel_litre
if 20 < fuel_litre <= 25:
    total_sum *= 0.92
elif fuel_litre > 25:
    total_sum *=0.9
print(f'{total_sum:.2f} lv.')

