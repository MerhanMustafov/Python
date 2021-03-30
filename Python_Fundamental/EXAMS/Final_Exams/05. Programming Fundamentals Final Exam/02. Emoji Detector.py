import re

text = input()

matches = re.findall(r"\d", text)
matches = [int(matches[x]) for x in range(len(matches))]
threshold = 1
for number in range(len(matches)):
    threshold *= matches[number]
print(f"Cool threshold: {threshold}")

pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"
valid_emojis = re.findall(pattern, text)
count_emojis = len(valid_emojis)
print(f"{count_emojis} emojis found in the text. The cool ones are:")

for num in range(len(valid_emojis)):
    lst = list(map(str, valid_emojis[num][1]))
    sum = 0
    for letter in lst:
        sum += ord(letter)
    n = num
    if sum >= threshold:
        print(''.join(valid_emojis[n]))

