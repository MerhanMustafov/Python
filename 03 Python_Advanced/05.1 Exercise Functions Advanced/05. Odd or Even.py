###-This is GREAT example for good usage of functions-###

def odd(nums):
    return sum([num for num in nums if num % 2 != 0]) * len(nums)

def even(nums):
    return sum([num for num in nums if num % 2 == 0]) * len(nums)

command = input()
list_of_numbers = [int(num) for num in input().split()]

if command == "Odd":
    print(odd(list_of_numbers))
elif command == "Even":
    print(even(list_of_numbers))