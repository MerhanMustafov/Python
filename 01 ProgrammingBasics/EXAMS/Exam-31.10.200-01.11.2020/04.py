number_student = int(input())

top_students = 0
between1 = 0
between2 = 0
fail = 0
sum = 0

for students in range(1, number_student + 1):
    grade = float(input())
    if 5.00 <= grade <= 6.00:
        top_students += 1
        sum += grade
    elif 4.00 <= grade <= 4.99:
        between1 += 1
        sum += grade
    elif 3.00 <= grade <= 3.99:
        between2 += 1
        sum += grade
    elif grade < 3.00:
        fail += 1
        sum += grade

percent_top_students = top_students / number_student * 100
percent_between1 = between1 / number_student * 100
percent_between2 = between2 / number_student * 100
percent_fail = fail / number_student * 100
average = sum / number_student

print(f"Top students: {percent_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_between1:.2f}%")
print(f"Between 3.00 and 3.99: {percent_between2:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {average:.2f}")