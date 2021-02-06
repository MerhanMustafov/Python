def negativ_positive_or_zero(num_one, num_two, num_three):
    num_lst = [num_one, num_two, num_three]
    pos = 0
    neg = 0
    zero = 0
    for digit in num_lst:
        if digit == 0:
            return "zero"
        if digit < 0:
            neg += 1
        else:
            pos += 1
    if neg % 2 ==0:
        return "positive"
    if not neg % 2 == 0:
        return "negative"
    if pos == 3:
        return "positive"

one = int(input())
two = int(input())
three = int(input())
result = negativ_positive_or_zero(one, two, three)
print(result)