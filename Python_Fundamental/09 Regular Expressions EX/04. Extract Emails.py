import re
text = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"
valid = [el.group() for el in re.finditer(pattern, text)]
print(*valid, sep="\n")