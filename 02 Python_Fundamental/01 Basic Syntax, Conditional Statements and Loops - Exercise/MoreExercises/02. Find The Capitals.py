word = input()
capitals = []

for letter in range (len(word)):
    position = word[letter]
    if 65 <= ord(position) <= 90:
        capitals.append(letter)
    else:
        continue
print(capitals)