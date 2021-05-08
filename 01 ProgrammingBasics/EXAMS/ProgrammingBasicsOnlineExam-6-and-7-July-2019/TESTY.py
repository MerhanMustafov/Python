from math import floor
word = input()

the_most_powerful_word = 0
best_word = word
vowel = False

while word != 'End of words':

    current_word = 0
    for letter in range(len(word)):
        position = word[letter]
        value = ord(position)
        current_word += value
        if letter == 0:
            if position == 'a' or position == 'e' or position == 'i':
                vowel = True
            elif position == 'o' or position == 'u' or position == 'y':
                vowel = True
            elif position == 'A' or position == 'E' or position == 'I':
                vowel = True
            elif position == 'O' or position == 'U' or position == 'Y':
                vowel = True
    if vowel:
        current_word *= len(word)
        current_word = floor(current_word)
    else:
        current_word /= len(word)
        current_word = floor(current_word)
    if current_word >= the_most_powerful_word:
        the_most_powerful_word = current_word
        best_word = word

    word = input()
print(f"The most powerful word is {best_word} - {the_most_powerful_word}")
