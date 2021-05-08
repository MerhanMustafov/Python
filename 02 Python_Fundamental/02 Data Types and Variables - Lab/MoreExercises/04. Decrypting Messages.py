key = int(input())
n = int(input())
descripted = ""
for line in range(n):
    char = input()
    if char == char.lower():
        digit = ord(char) + key
        descripted += chr(digit)

    elif char == char.upper():
        digit = ord(char) + key
        descripted += chr(digit)
print(descripted)