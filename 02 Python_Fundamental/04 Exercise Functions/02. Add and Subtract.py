def sum_num(num_one, num_two):
    return num_one + num_two

def sum_subtract(three):
    result = sum_num(num_one, num_two)
    subract = result - num_three
    return subract

def add_and_subract(num_one, num_two, num_three):
    sum = sum_num(num_one, num_two)
    subract = sum_subtract(num_three)
    return subract


num_one = int(input())
num_two = int(input())
num_three = int(input())

print(add_and_subract(num_one, num_two, num_three))