import re
pattern = r"(^=|\/)([A-Za-z]{3,})\1"
text = input()
text = re.findall(pattern, text)
print(text)