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
    return (f"Odd sum = {odd}, Even sum = {even}")


number = int(input())
print(sum_of_even_and_odd_nums(number))