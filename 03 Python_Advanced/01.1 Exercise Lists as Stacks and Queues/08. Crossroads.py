from collections import deque

green_light = int(input())
window = int(input())

cars = deque()
cars_counter = 0
crashed = False

command = input()

while command != "END":
    if command == "green":
        if cars:
            current = cars.popleft()
            seconds_left = green_light - len(current)
            while seconds_left > 0:
                cars_counter += 1
                if cars:
                    current = cars.popleft()
                    seconds_left -= len(current)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                idx = window + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[idx]}.")
                crashed = True
                break
    else:
        cars.append(command)
    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")



# TODO - gives 71/100
# from collections import deque
# green_light = int(input())
# free_interval = int(input())
#
# total_cars = deque([])
# is_hit = False
# total_passed_cars = 0
#
#
# command = input()
# while not command == "END":
#
#     if not command == "green":
#         total_cars.append(command)
#
#     else:
#         hit_car = total_cars[0]
#         current_car = deque(total_cars.popleft())
#         cur_car_light_counter = 0
#         cur_car_free_counter = 0
#
#         while current_car:
#             current_car.popleft()
#             cur_car_light_counter += 1
#             if cur_car_light_counter == green_light and current_car:
#                 while current_car:
#                     current_car.popleft()
#                     cur_car_free_counter += 1
#                     if cur_car_free_counter == free_interval and current_car:
#                         hit_place = current_car[0]
#                         is_hit = True
#                         print(f"A crash happened!\n{hit_car} was hit at {hit_place}.")
#                         exit(0)
#                 total_passed_cars += 1
#
#
#             elif not current_car:
#                 total_passed_cars += 1
#                 if cur_car_light_counter < green_light and total_cars:
#                     hit_car = total_cars[0]
#                     current_car = deque(total_cars.popleft())
#                     continue
#
#
#     command = input()
#
#
# print(f"Everyone is safe.\n{total_passed_cars} total cars passed the crossroads.")
