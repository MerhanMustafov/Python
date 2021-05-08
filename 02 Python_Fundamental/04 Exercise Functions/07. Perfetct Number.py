def sum_of_proper_positive_divisors(number):
    sum_of_digits = 1
    for num in range(2, number - 1):
        if number % num == 0:
            sum_of_digits += num
    if sum_of_digits == number:
        return "We have a perfect number!"
    else:
        return " It's not so perfect."

number = int(input())
print(sum_of_proper_positive_divisors(number))