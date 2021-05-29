def positive_nums(num):
    return [str(x) for x in num if x >= 0]
def negative_nums(num):
    return [str(x) for x in num if x < 0]
def even_nums(num):
    return [str(x) for x in num if x % 2 == 0]
def odd_nums(num):
    return [str(x) for x in num if x % 2 != 0]

numbers = [int(n) for n in input().split(", ")]
print(f"Positive: {', '.join(positive_nums(numbers))}")
print(f"Negative: {', '.join(negative_nums(numbers))}")
print(f"Even: {', '.join(even_nums(numbers))}")
print(f"Odd: {', '.join(odd_nums(numbers))}")
