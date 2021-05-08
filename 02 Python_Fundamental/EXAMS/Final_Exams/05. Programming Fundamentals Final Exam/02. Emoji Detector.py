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

# import re
#
# text = input()
#
# pattern = r"(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})(\1)"
# valid_emojis = [match.group() for match in re.finditer(pattern, text)]
# cool_threshold = 1
# for i in text:
#     if i.isdigit():
#         i = int(i)
#         cool_threshold *= i
# print(f"Cool threshold: {cool_threshold}")
# print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
#
# for el in valid_emojis:
#     sum_of_letters = 0
#     for char in el:
#         if char.isalpha():
#             sum_of_letters += ord(char)
#     if sum_of_letters >= cool_threshold:
#         print(el)