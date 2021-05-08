inherited_money = float(input())
year_to_live = int(input())
spended_money = 12000
maded_years = 17

for years in range(1800, year_to_live + 1):
    maded_years +=1
    if years % 2 == 0:
        inherited_money -= spended_money
    else:
        spended = spended_money + 50 * maded_years
        inherited_money -= spended
if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")