unsatisfy_grades = int(input())

name_task = input()
number_solved = 0
average = 0
failed = 0
last_one = name_task

time_to_breake = False
while name_task != "Enough":
    task_grade = int(input())
    if task_grade <= 4:
        failed += 1
        if failed == unsatisfy_grades:
            print(f"You need a break, {failed} poor grades.")
            break

    average += task_grade
    number_solved += 1
    last_one = name_task
    name_task = input()


else:

    print(f"Average score: {float(average / number_solved):.2f}")
    print(f"Number of problems: {number_solved}")
    print(f"Last problem: {last_one}")




# maxsimum_bad_grades = int(input())
# total_score = 0
# number_of_problems = 0
# last_problem = ""
# number_of_bad_grades = 0
# toomany_bad_grades = False
# comand = input()
# while comand != 'Enough':
#     last_problem = comand
#     current_grade = int(input())
#     if current_grade <= 4:
#         number_of_bad_grades += 1
#         if number_of_bad_grades == maxsimum_bad_grades:
#             toomany_bad_grades = True
#             break
#     number_of_problems += 1
#     total_score += current_grade
#
#     comand = input()
# if toomany_bad_grades:
#     print(f"You need a break, {maxsimum_bad_grades} poor grades.")
# else:
#     average_score = total_score / number_of_problems
#     print(f"Average score: {average_score:.2f}")
#     print(f"Number of problems: {number_of_problems}")
#     print(f"Last problem: {last_problem}")
#
#
#
#
