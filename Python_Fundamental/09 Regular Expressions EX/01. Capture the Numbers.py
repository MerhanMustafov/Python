import re
pattern = r"\d+"
text = input()
all_matches = []
while not text == "":
    maches = re.findall(pattern, text)
    all_matches.extend(maches)
    text = input()
print(*all_matches)