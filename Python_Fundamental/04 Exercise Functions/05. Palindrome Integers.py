def palindrome_numbers(string_of_numbers):
    number = 0
    check_for_palindrome = []

    for num in range(len(string_of_numbers)):
        number = string_of_numbers[num]

        for digit in number:
            check_for_palindrome.append(digit)
        check_for_palindrome.reverse()
        check_for_palindrome = list(map(int, check_for_palindrome))
        number = list(map(int, number))
        if number == check_for_palindrome:
            print(True)
        else:
            print(False)

        check_for_palindrome = []

string_of_numbers = input().split(", ")
palindrome_numbers(string_of_numbers)