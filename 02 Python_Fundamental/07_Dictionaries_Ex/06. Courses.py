command = input()
data = {}
while not command == "end":
    command = command.split(" : ")
    course = command[0]
    if course not in data:
        data[course] = []
    student = command[1]
    data[course].append(student)

    command = input()
data = dict(sorted(data.items(), key=lambda kvp: -len(kvp[1])))
for course_type, student_name in data.items():
    print(f"{course_type}: {len(data[course_type])}")
    data[course_type] = sorted(data[course_type])
    for name in range(len(data[course_type])):
        student_name = data[course_type][name]
        print(f"-- {student_name}")
