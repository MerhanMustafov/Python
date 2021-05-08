
def same_word(word, n):
    result = ""
    for i in range(n):
        result += word
    return result
word = input()
n = int(input())
print(same_word(word, n))

# # my solution after the final exam and course
# def repeating_string(string, n):
#     return string * n
#
# string = input()
# num = int(input())
# print(repeating_string(string, num))
