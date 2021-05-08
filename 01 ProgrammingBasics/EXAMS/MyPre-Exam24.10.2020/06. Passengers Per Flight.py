import sys
import math
num_airlines = int(input())
most_pass = -sys.maxsize
name_best = ''

for airlines in range(1, num_airlines +1):
    current_airline = input()

    total_passangers = 0
    count = 0
    command = input()
    while command != 'Finish':
        passangers = int(command)
        total_passangers += passangers
        count+=1
        command = input()
    average = math.floor(total_passangers / count)
    print(f"{current_airline}: {average} passengers.")
    if average > most_pass:
        most_pass = average
        name_best = current_airline
print(f"{name_best} has most passengers per flight: {most_pass}")