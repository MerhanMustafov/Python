
def same_word(word, n):
    result = ""
    for i in range(n):
        result += word
    return result
word = input()
n = int(input())
print(same_word(word, n))
