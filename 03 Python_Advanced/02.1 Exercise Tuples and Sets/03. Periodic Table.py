def collectin_in_set(n):
    s = set()
    for _ in range(n):
        command = input().split(" ")
        for ch_compound in command:
            s.add(ch_compound)
    return s

n = int(input())
for character in collectin_in_set(n):
    print(character)



