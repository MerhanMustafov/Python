target_steps = 10000
command = input()
sum_steps = 0
is_reached = False
while command != 'Going home':
    number = int(command)
    sum_steps += number
    if sum_steps >= target_steps:
        is_reached = True
        break
    command = input()
if is_reached:
    result = abs(sum_steps - target_steps)
    print("Goal reached! Good job!")
    print(f"{result} steps over the goal!")
if command == 'Going home':
    way_back_home = int(input())
    sum_steps += way_back_home
    if sum_steps < target_steps:
        result = target_steps - sum_steps
        print(f'{result} more steps to reach goal.')
    elif sum_steps > target_steps:
        result = abs(sum_steps - target_steps)
        print("Goal reached! Good job!")
        print(f"{result} steps over the goal!")

# steps = 10000
# sum_steps = 0
# steps_over = abs(sum_steps - steps)
#
# command = input()
# is_going_home = False
# while sum_steps < steps:
#     if command == "Going home":
#         is_going_home = True
#         more_steps = int(input())
#         sum_steps+= more_steps
#         if sum_steps < steps:
#             print(f"{abs(steps - sum_steps)} more steps to reach goal.")
#             break
#         else:
#             print("Goal reached! Good job!")
#             print(f"{abs(sum_steps - steps)} steps over the goal!")
#             break
#     passed_steps = int(command)
#     sum_steps += passed_steps
#     if sum_steps >= steps:
#         break
#     command = input()
# if not is_going_home:
#     print("Goal reached! Good job!")
#     print(f"{abs(sum_steps - steps)} steps over the goal!")