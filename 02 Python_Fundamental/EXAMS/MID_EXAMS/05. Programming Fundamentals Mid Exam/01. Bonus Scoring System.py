students_num = int(input())
lextures_count = int(input())
initial_bonus = int(input())

highest_attendance = 0
max_bonus = 0

for each_student in range(students_num):
    student_attendances = int(input())
    total_bonus = (student_attendances / lextures_count) * (5 + initial_bonus)

    if highest_attendance < student_attendances:
        highest_attendance = student_attendances
        max_bonus = total_bonus
print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {round(highest_attendance)} lectures.")