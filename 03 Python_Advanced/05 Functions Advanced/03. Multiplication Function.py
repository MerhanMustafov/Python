from functools import reduce

def multiply(*args):
    return reduce(lambda x, y: x*y, args)

# print(multiply(4, 5, 6, 1, 3))


