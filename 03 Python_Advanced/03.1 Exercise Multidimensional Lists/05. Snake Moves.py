def reverse_string(current_word):
    return current_word[::-1]

from collections import deque
rows, cols = [int(el) for el in input().split(" ")]

word = deque([el for el in input()])

for row_ind in range(rows):
    current_word = ""
    for index in range(cols):
        current_word += word[0]
        word.append(word.popleft())
    if not row_ind % 2 == 0:
        current_word = reverse_string(current_word)
    print(current_word)

