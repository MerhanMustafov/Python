
def the_smallest_num(num_one, num_two, num_three):
    result =min(num_one, num_two, num_three)
    return result

num_one = int(input())
num_two = int(input())
num_three = int(input())

print(the_smallest_num(num_one, num_two, num_three))

# # solution after the cpurse
# def smallest_of_three_numbers(first, second, third):
#     lst = [first, second, third]
#     lst.sort()
#     return lst[:1]
#
# first = int(input())
# second = int(input())
# third = int(input())
# result = smallest_of_three_numbers(first, second, third)
# print(*result)