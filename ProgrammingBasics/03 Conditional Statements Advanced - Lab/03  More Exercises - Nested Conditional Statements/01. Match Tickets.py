from math import fabs
budget = float(input())
category = input()
number_of_people = int(input())
ticket_VIP = 499.99
ticket_Normal = 249.99
total_tickets = 0
if category == "VIP":
    total_tickets = ticket_VIP * number_of_people
    if 1 <= number_of_people <= 4:
        budget = budget - (budget * 0.75)
    elif 5 <= number_of_people <= 9:
        budget = budget - (budget * 0.6)
    elif 10 <= number_of_people <= 24:
        budget = budget - (budget * 0.5)
    elif 25 <= number_of_people <= 49:
        budget = budget - (budget * 0.4)
    elif number_of_people >= 50:
        budget = budget - (budget * 0.25)
elif category == "Normal":
    total_tickets= ticket_Normal * number_of_people
    if 1 <= number_of_people <= 4:
        budget = budget - (budget * 0.75)
    elif 5 <= number_of_people <= 9:
        budget = budget - (budget * 0.6)
    elif 10 <= number_of_people <= 24:
        budget = budget - (budget * 0.5)
    elif 25 <= number_of_people <= 49:
        budget = budget - (budget * 0.4)
    elif number_of_people >= 50:
        budget = budget - (budget * 0.25)

remains = budget - total_tickets
if budget >= total_tickets:
    print(f"Yes! You have {fabs(remains):.2f} leva left.")
else:
    print(f"Not enough money! You need {fabs(remains):.2f} leva.")

