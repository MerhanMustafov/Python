import re
text = input()
pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

vallid_variable = [obj.group()for obj in re.finditer(pattern, text)]
print(*vallid_variable, sep=",")