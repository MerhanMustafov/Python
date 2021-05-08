n = int(input())
tracking = {}
for el in range(0, n*2, 2):
    name = input()
    grade = float(input())
    if name not in tracking:
        tracking[name] = []
    tracking[name].append(grade)
delete = []
for student, grades in tracking.items():
    average = sum(grades) / len(grades)
    if not average >= 4.50:
        delete.append(student)
for i in delete:
    del tracking[i]
tracking = dict(sorted(tracking.items(), key=lambda x: sum(x[1])/ len(x[1]), reverse=True))
for a, b in tracking.items():
    print(f"{a} -> {sum(b)/ len(b):.2f}")

