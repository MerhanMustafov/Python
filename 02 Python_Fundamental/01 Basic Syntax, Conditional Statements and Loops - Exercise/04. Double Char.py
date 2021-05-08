word = input()
sensitive_new_word = ''
# for letter in range (len(word)):
#     sensitive_new_word += word[letter]*2
# print(sensitive_new_word)

for char in word:
    sensitive_new_word += char*2
print(sensitive_new_word)