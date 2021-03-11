word = input().split()
final_word = ""
for w in word:
    final_word += w * len(w)
print(final_word)