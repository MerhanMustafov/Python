
def the_smallest_num(num_one, num_two, num_three):
    result =min(num_one, num_two, num_three)
    return result

num_one = int(input())
num_two = int(input())
num_three = int(input())

print(the_smallest_num(num_one, num_two, num_three))