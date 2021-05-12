def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


n = int(input())
student_grades_lines = input_to_list(n)


def avr(value):
    return sum(value) / len(value)


student_grades = {}

for line in student_grades_lines:
    student, grade = line.split(" ")
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(float(grade))

for student, grades in student_grades.items():
    grades_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    avg_grade = avr(grades)
    print(f"{student} -> {grades_string} (avg: {avg_grade:.2f})")
