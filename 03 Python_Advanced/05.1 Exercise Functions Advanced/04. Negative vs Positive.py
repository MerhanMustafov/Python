def negative_vs_positive(numbers):
    sum_negative = sum([n for n in numbers if n < 0])
    print(sum_negative)
    sum_positive = sum([p for p in numbers if p >= 0])
    print(sum_positive)
    if sum_positive > abs(sum_negative):
        return True
    else:
        return False

numbers = [int(el) for el in input().split()]
result = negative_vs_positive(numbers)
if result:
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")