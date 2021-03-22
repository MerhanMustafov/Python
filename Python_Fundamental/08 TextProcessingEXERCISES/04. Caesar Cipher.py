string = list(map(str, input()))
for position in range(len(string)):
    replace = ord(string[position]) + 3
    string[position] = chr(replace)
print("".join(string))

# https://pastebin.com/pnNJDLqv