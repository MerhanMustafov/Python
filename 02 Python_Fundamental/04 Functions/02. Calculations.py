def simple_calculator(operator, num_1, num_2):
    if operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return  num_1 // num_2
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2
oper = input()
number_1 = int(input())
number_2 = int(input())

print(simple_calculator(oper, number_1, number_2 ))


# # My solution, after final exam and end of the course
# def calculation(one, two, string):
#     result = 0
#     if string == "multiply":
#         result = one * two
#     elif string == "divide":
#         result = one // two
#     elif string == "add":
#         result = one + two
#     elif string == "subtract":
#         result = one - two
#     return result
#
# string = input()
# first_num = int(input())
# second_num = int(input())
# print(calculation(first_num, second_num, string))