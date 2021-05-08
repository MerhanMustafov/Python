employee_cap_one = int(input())
employee_cap_two = int(input())
employee_cap_three = int(input())

total_people = int(input())

cap_per_hour = employee_cap_one + employee_cap_two + employee_cap_three
hours = 0
while total_people > 0:

    total_people -= cap_per_hour
    hours += 1
    if hours % 4 == 0 and hours > 0:
        hours += 1
        continue
print(f"Time needed: {hours}h.")