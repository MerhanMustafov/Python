one = int(input())
two = int(input())
three = int(input())

total_employee_capacity = one + two + three
student_count = int(input())
hours = 0
while student_count > 0:
    student_count -= total_employee_capacity
    hours += 1
    if hours % 4 == 0:
        hours += 1
        continue
print(f"Time needed: {hours}h.")
