import re
pattern = r"(@|\#)([a-zA-Z][a-zA-Z][a-zA-Z]+)\1\1([a-zA-Z][a-zA-Z][a-zA-Z]+)\1"
    # r"(@|\#)(?P<first>[a-zA-Z][a-zA-Z][a-zA-Z]+)\1\1(?P<socond>[a-zA-Z][a-zA-Z][a-zA-Z]+)\1"
text = input()
matches = re.findall(pattern, text)
count = len(matches)
mirror_words = []
for match in matches:
    first = match[1]
    second = match[2]
    if first == second[::-1]:
        mirror_words.append([first, second])
if count > 0:
    print(f"{count} word pairs found!")
else:
    print(f"No word pairs found!")
if mirror_words:
    print(f"The mirror words are:")
    for words in range(len(mirror_words)):
        s = mirror_words[words]
        if not len(mirror_words) - 1 == words:
            print(f"{s[0]} <=> {s[1]},", end=" ")
        else:
            print(f"{s[0]} <=> {s[1]}", end="")

else:
    print(f"No mirror words!")

