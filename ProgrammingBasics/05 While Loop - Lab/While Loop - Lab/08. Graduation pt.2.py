student_name = input()
fails = 0
current_class = 0
total_grade = 0
isEjected = False

while current_class < 12:

    current_grade = float(input())
    if current_grade < 4:
      fails +=1
    if fails == 2:
        isEjected = True
        break
    else:
        total_grade += current_grade
        if current_class == 12:
            break
        current_class += 1
if isEjected:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = total_grade / current_class
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")