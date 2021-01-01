name = input()
current_class = 0
fail = 0
total_grade = 0
number = 0

while current_class < 12:
    current_grade = float(input())
    if current_grade >= 4:
        number += 1
        total_grade += current_grade
    else:
        fail += 1
    if fail == 2:
        print(f"{name} has been excluded at {current_class} grade")
        break
    current_class += 1
else:

    print(f"{name} graduated. Average grade: {total_grade / number:.2f}")