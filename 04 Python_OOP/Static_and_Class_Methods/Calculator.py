class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for n in args:
            result *= n
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for n in args[1:]:
            result /= n
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for n in args[1:]:
            result -= n
        return result

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))




# from functools import reduce
# class Calculator:
#     @staticmethod
#     def add(*args):
#         return sum(args)
#     @staticmethod
#     def multiply(*args):
#         return reduce(lambda x, y: x * y, args)
#     @staticmethod
#     def divide(*args):
#         return reduce(lambda x, y: x / y, args)
#     @staticmethod
#     def subtract(*args):
#         return reduce(lambda x, y: x - y, args)
#
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))
