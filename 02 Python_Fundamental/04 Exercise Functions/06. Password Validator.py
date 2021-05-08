def pass_validation(list_password):
    list_password = list(map(str, list_password))
    character_length = len(list_password)
    only_letters_and_digits = True
    num_of_digits = 0

    for character in list_password:
        if character.isdigit():
            num_of_digits += 1
            continue
        if not character.isalpha():
            only_letters_and_digits = False

    if (only_letters_and_digits) and (num_of_digits >= 2) and (6 <= character_length <= 10):
        print("Password is valid")
    else:
        if not only_letters_and_digits:
            print("Password must consist only of letters and digits")
        if not 6 <= character_length <= 10:
            print("Password must be between 6 and 10 characters")
        if num_of_digits < 2:
            print("Password must have at least 2 digits")

password = input()
pass_validation(password)