n = int(input())
word = input()
string = []

for x in range(n):
    curreent_str = input()
    string.append(curreent_str)
print(string)
for i in range(len(string) -1, -1, -1):
    element = string[i]
    if word not in element:
        string.remove(element)
print(string)
