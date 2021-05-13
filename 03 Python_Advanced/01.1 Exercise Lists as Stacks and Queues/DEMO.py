def interval(current_car, free_interval, is_hit):
    counter = 0
    while counter < free_interval:
        current_car.popleft()
        counter += 1
        if not current_car:
            break
    if current_car:
        is_hit = True
        return current_car[0]

def lights_on(green_light, car_passed):
    car_passed = 0
    current_car = deque(map(str, cars.popleft()))
    counter = 0
    while counter < green_light:
        current_car.popleft()
        counter += 1
        if not current_car:
            car_passed += 1
            if not cars:
                break
            current_car = deque(map(str, cars.popleft()))
    if cars:
        interval(current_car, free_interval, is_hit)


def filling_the_cars_list(command, cars):
    cars.append(command)
    return cars



from collections import deque
green_light = int(input())
free_interval = int(input())
is_hit = False
cars = deque([])
command = input()

passed = 0
while not command == "END":
    if not command == "green":
        cars = filling_the_cars_list(command, cars)
    else:
        lights_on(green_light, passed)
    if is_hit == True:
        break
    command = input()

if is_hit == True:
    print(f"Crash")
else:
    print(f"Everyone is safe.\n ")




