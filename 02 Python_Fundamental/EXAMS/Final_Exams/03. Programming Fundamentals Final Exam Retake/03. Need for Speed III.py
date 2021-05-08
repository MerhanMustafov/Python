n = int(input())
cars_data = {}

for _ in range(n):
    info_car = input().split("|")
    car = info_car[0]
    mileage = int(info_car[1])
    fuel_available = int(info_car[2])
    cars_data[car] = {"mileage": mileage, "fuel_available": fuel_available}


command = input()
while not command == "Stop":
    command = command.split(" : ")

    if command[0] == "Drive":
        cur_car = command[1]
        cur_distance = int(command[2])
        cur_fuel = int(command[3])
        if cars_data[cur_car]['fuel_available'] < cur_fuel:
            print(f"Not enough fuel to make that ride")
        else:
            cars_data[cur_car]['mileage'] += cur_distance
            cars_data[cur_car]['fuel_available'] -= cur_fuel
            print(f"{cur_car} driven for {cur_distance} kilometers. {cur_fuel} liters of fuel consumed.")
            if cars_data[cur_car]['mileage'] >= 100000:
                cars_data.pop(cur_car)
                print(f"Time to sell the {cur_car}!")

    elif command[0] == "Refuel":
        cur_car = command[1]
        fuel_state = cars_data[cur_car]['fuel_available']
        fuel_to_refill = int(command[2])
        if (fuel_to_refill + fuel_state) > 75:
            left_to_refill = 75 - fuel_state
            cars_data[cur_car]['fuel_available'] += left_to_refill
            print(f"{cur_car} refueled with {left_to_refill} liters")
        else:
            cars_data[cur_car]['fuel_available'] += fuel_to_refill
            print(f"{cur_car} refueled with {fuel_to_refill} liters")

    elif command[0] == "Revert":
        cur_car = command[1]
        km = int(command[2])
        cars_data[cur_car]['mileage'] -= km
        if cars_data[cur_car]['mileage'] < 10000:
            cars_data[cur_car]['mileage'] = 10000
            command = input()
            continue
        else:
            print(f"{cur_car} mileage decreased by {km} kilometers")

    command = input()


cars_data = sorted(cars_data.items(), key=lambda kdv: (-kdv[1]['mileage'], kdv[0]))
for a_car, info_data in cars_data:
    print(f"{a_car} -> Mileage: {info_data['mileage']} kms, Fuel in the tank: {info_data['fuel_available']} lt.")