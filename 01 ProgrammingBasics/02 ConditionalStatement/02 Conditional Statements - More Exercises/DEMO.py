vacation_price = float(input())
puzzles_number = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions_number = int(input())
trucks_number = int(input())
number_of_toy = puzzles_number + talking_dolls +teddy_bears +minions_number +trucks_number
amount_of_money_after_sales = puzzles_number * 2.60 + talking_dolls * 3 + teddy_bears * 4.10 + minions_number * 8.20 + trucks_number * 2


if number_of_toy >= 50:
    amount_of_money_after_sales *= 0.75
amount_of_money_after_sales *= 0.9
if amount_of_money_after_sales >= vacation_price:
    print(f'Yes! {(amount_of_money_after_sales - vacation_price):.2f} lv left.')
else:
    print(f'Not enough money! {(vacation_price - amount_of_money_after_sales ):.2f} lv needed.')