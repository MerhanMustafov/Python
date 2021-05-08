words = [w.lower()for w in input().split()]
occurances = {}
for word in words:
    occurances[word] = words.count(word)
for key, value in occurances.items():
    if not occurances[key] % 2 == 0:
        print(f"{key}", end=" ")
