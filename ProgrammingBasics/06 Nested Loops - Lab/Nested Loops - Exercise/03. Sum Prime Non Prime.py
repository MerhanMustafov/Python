sum_of_prime_num = 0
sum_of_non_prime_num = 0
command = input()
while command != 'stop':
    isPrime = True
    number = int(command)
    if number < 0:
        print('Number is negative.')
        command = input()
        continue
    for checking in range(2, number):
        if number % checking == 0:
            isPrime = False
            break
    if isPrime:
        sum_of_prime_num += number
    else:
        sum_of_non_prime_num += number
    command = input()
print(f"Sum of all prime numbers is: {sum_of_prime_num}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_num}")