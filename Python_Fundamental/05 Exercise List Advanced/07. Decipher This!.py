secret_mes = input().split(" ")

for part in range(len(secret_mes)):
    word = list(map(str, secret_mes[part]))
    # print(word)
    digit = [dig for dig in word if dig.isdigit()]
    num_digit = len(digit)
    # print(num_digit)
    digit = int("".join(digit))
    digit_to_letter = chr(digit)
    # print(digit_to_letter)
    if num_digit == 2:
        word.remove(word[0])
        word.remove(word[0])
        word.insert(0, digit_to_letter)
        word[1], word[-1] = word[-1], word[1]

    elif num_digit == 3:
        word.remove(word[0])
        word.remove(word[0])
        word.remove(word[0])
        word.insert(0, digit_to_letter)
        word[1], word[-1] = word[-1], word[1]
    print("".join(word), end=" ")
