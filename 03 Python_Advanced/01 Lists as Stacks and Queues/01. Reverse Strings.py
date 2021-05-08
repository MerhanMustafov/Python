# string = list(map(str, input()))
# new_str = ""
# while string:
#     new_str += string.pop()
# print(new_str)

text = input()

s = []
for ch in text:
    s.append(ch)

result = ''
while s:
    result += s.pop()
print(result)
