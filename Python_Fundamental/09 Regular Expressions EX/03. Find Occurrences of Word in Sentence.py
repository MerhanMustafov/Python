import re

text = input()
search_word = input()


pattern = rf"\b{search_word}\b"
count_word = re.findall(pattern, text, re.IGNORECASE)
print(len((count_word)))