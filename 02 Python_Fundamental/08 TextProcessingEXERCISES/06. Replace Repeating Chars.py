str_letters = input()

index = 0
while index < len(str_letters) -1:
    if str_letters[index] == str_letters[index+1]:
        to_replace = f"{str_letters[index]}{str_letters[index+1]}"
        str_letters = str_letters.replace(to_replace, str_letters[index])
        index = 0
    else:
        index += 1
print(str_letters)

# https://pastebin.com/cbbQHFjV