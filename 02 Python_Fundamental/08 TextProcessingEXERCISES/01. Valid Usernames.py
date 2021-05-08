import re
user_names = input().split(", ")
for name in user_names:
    if 3 <= len(name) <= 16:
        if bool(re.match("^[A-Za-z0-9_-]*$", name)):
            print(name)