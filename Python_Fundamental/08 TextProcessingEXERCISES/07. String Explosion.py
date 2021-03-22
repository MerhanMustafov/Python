string = list(map(str, input()))
count = string.count(">")
index = 0
print(count)
left = 0
while count > 0:
    if string[index] == ">":
        start = index + 1
        stop = start + int(string[index + 1])
        left = int(string[index + 1])
        for ch in range(start, stop+1):
            if string[ch] == ">":
                string[index + 2] = (string[index + 2] + left)
                index = ch
                count -= 1
                break
            else:
                string[ch] = "N"
                left -= 1

    else:
        index += 1
