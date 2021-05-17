def red_light(cars, command):
    cars = []
    while not command == "green":
        cars.append(command)
        command = input()
    return cars, command
def yellow_light(cur_car, sec_yellow, num_passed, is_carsh, letter):
    count = 0
    while count < sec_yellow:
        cur_car.popleft()
        count += 1
        if not cur_car:
            num_passed += 1
            return num_passed, is_carsh, letter
    if cur_car:
        is_carsh = True
        letter = cur_car[0]
        return num_passed, is_carsh, letter
def green(cars, sec_green, num_passed, is_carsh, letter):
    hit_car = cars[0]
    current_car = deque(cars.popleft())
    count = 0
    while count < sec_green:
        current_car.popleft()
        count += 1
        if not current_car:
            num_passed += 1
            if cars:
                hit_car = cars[0]
                current_car = deque(cars.popleft())
            else:
                break
    if current_car:
       num_passed, is_carsh, letter = yellow_light(current_car, sec_yellow, num_passed, is_carsh, letter)
    return cars, input(), num_passed, hit_car, is_carsh, letter

from collections import deque
sec_green = int(input())
sec_yellow = int(input())

cars = deque([])
num_passed = 0
hit_car = None
letter = None
is_carsh = False
command = input()
while not command == "END":

    if not command == "green":
       cars, command =  red_light(cars, command)
    elif command == "green":
        cars, command, num_passed, hit_car, is_carsh, letter = green(deque(cars), sec_green,num_passed, is_carsh, letter)
        if is_carsh:
            break
if is_carsh:
    print(f"A crash happened!\n{hit_car} was hit at {letter}.")
else:
    print(f"Everyone is safe.\n{num_passed} total cars passed the crossroads.")