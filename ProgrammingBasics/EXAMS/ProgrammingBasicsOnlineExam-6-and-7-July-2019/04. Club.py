import sys
desired_income = float(input())

command = input()
current = 0
while command != "Party!":
    number_cocktails = int(input())
    total = len(command) * number_cocktails

    if total % 2 != 0:
        total *= 0.75
    current += total
    if current >= desired_income:
        print("Target acquired.")
        print(f"Club income - {current:.2f} leva.")
        sys.exit(0)
    command = input()
print(f"We need {abs(desired_income-current):.2f} leva more.")
print(f"Club income - {current:.2f} leva.")