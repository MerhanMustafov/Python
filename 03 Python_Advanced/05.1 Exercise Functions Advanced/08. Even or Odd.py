def str_to_int(args):
    return [int(n) for n in args[0:-1]]
def even_odd(*args):
    command = args[-1]
    if command == "even":
        return list(filter(lambda num: num % 2 ==0, str_to_int(args)))
    elif command == "odd":
        return list(filter(lambda num: num % 2 != 0, str_to_int(args)))

# string = [el for el in input().split()]
# print(even_odd(string))
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))