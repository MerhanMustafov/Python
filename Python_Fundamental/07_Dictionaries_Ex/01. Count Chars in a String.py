charactars = [x for x in input()]

dictionary = {}
for chrar in charactars:
    if chrar == " ":
        continue
    dictionary[chrar] = charactars.count(chrar)
for key, value in dictionary.items():
    print(f"{key} -> {dictionary[key]}")