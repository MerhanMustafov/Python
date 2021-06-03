# def even_nums(numbers):
#     return [num for num in numbers if num % 2 == 0]
numbers = list(map(int, input().split(" ")))
# print(even_nums(numbers))
print(list(filter(lambda num: (num % 2 == 0 ), numbers)))
