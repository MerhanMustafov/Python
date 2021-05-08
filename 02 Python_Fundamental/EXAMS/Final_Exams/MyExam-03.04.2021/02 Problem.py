import re

pattern = r"([a-zA-Z0-9]+|\W+)>(\d\d\d)(\|)([a-z][a-z][a-z])\3([A-Z][A-Z][A-Z])\3([^\<\>][^\<\>][^\<\>])<\1"
# pattern = f"([a-zA-Z0-9]+|\W+)>\d{3}(\|)[a-z]{3}\2[A-Z]{3}\2[^\<\>+]{3}<\1"
n = int(input())
for _ in range(n):
    line = input()
    mach = re.findall(pattern, line)
    if mach:
        mach = mach[0]
        final = ""
        for one in range(len(mach)):
            if one == 0:
                continue
            else:
                if mach[one] == "|":
                    continue
                final += mach[one]
        print(f"Password: {final}")
    else:
        print(f"Try another password!")
