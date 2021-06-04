def palindrome(word, index = 0):
    if word == word[::-1]:
        return (f"{word} is palindrome")
    elif word != word[::-1]:
        return (f"{word} is not a palindrome")

    for i in range(index, len(word)):
        word[index], word[i] = word[i], word[index]
        palindrome(word, index)
        word[index], word[i] = word[i], word[index]

print(palindrome("acba", 0))
print(palindrome("peter", 0))

