def calculate_combin(names, n, combinations=[]):
    if len(combinations) == n:
        print(", ".join(combinations))
        return

    for i in range(len(names)):
        name = names[i]
        combinations.append(name)
        calculate_combin(names[i+1:], n, combinations)
        combinations.pop()

names = input().split(", ")
n = int(input())
calculate_combin(names, n)

