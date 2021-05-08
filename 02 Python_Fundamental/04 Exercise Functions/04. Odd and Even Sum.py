def sum_of_even_and_odd_nums(number):
    odd = 0
    even = 0
    number = str(number)
    for num in range(len(number)):
        digit = int(number[num])
        if digit % 2 == 0:
            even += digit
        if digit % 2 != 0:
            odd += digit
    return [odd, even]


number = int(input())
result = sum_of_even_and_odd_nums(number)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")