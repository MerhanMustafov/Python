import re
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()
maches = [mach.group()for mach in re.finditer(pattern, text)]
print(*maches)
# for mach in maches:
#     print(mach.group(0), end=" ")
