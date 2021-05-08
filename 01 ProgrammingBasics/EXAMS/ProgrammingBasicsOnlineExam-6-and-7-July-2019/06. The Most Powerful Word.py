from math import floor

word = input()
current_total_word = 0
best_total = 0
best_word = word
vawal = False
while word != "End of words":

    for letter in range(len(word)):
        position = word[letter]
        value = ord(position)
        current_total_word += value
        if letter == 0:
            if position == 'a' or position == 'e' or position == 'i':
                vawal = True
            if position == 'o' or position == 'u' or position == 'y':
                vawal = True
            if position == 'A' or position == 'E' or position == 'I':
                vawal = True
            if position == 'O' or position == 'U' or position == 'Y':
                vawal = True
    if not vawal:
        current_total_word = current_total_word / len(word)

    if vawal:
        current_total_word = current_total_word * len(word)
    if current_total_word >= best_total:
        best_total = current_total_word
        best_word = word
    current_total_word = 0
    word = input()
print(f"The most powerful word is {best_word} - {floor(best_total)}")
