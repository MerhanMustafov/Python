import sys
lines = int(input())
sum = 0
for i in range(lines):
    if lines > 20:
        sys.exit(0)
    letter = input()
    if 65 <= ord(letter) <= 90:
        sum += ord(letter)
    elif 97 <= ord(letter) <= 122:
        sum += ord(letter)
print(f"The sum equals: {sum}")

