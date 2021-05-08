symbols = input()
digits = ""
letters = ""
other = ""
for symb in symbols:
    if symb.isdigit():
        digits += symb
    elif symb.isalpha():
        letters += symb
    else:
        other += symb
print(digits)
print(letters)
print(other)