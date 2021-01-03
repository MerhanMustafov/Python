command = input()

adults = 0
kids = 0


while command != 'Christmas':
    age = int(command)
    if age <= 16:
        kids += 1
    elif age > 16:
        adults += 1
    command = input()
money_for_toys = kids * 5
money_for_sweatener = adults * 15
print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweatener}")

