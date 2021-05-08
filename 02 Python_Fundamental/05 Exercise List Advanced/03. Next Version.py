version = input().split(".")
version = list(map(int, version))
for digit in range(len(version) -1, -1, -1):
    if version[digit] == 9:
        version[digit] = 0
        if version[digit - 1] == 9:
            version[digit - 1] = 0
            version[digit - 2] += 1
            break
        else:
            version[digit -1] += 1
            break
    else:
        version[digit] += 1
        break

version = list(map(str, version))
print(".".join(version))
