lines = input().split()
dictionary = {}

while lines:

    for el in range(0, len(lines), 2):
        key = lines[el + 1].lower()
        value = int(lines[el])
        if not key in dictionary:
            dictionary[key] = value
        else:
            dictionary[key] += value
    for k, v in dictionary.items():
        k.lower()
        if k == "shards":
            if dictionary[k] >= 250:
                print(f"{k} obtained!")
        if k == "fragments":
            if dictionary[k] >= 250:
                print(f"{k} obtained!")
        if k == "motes":
            if dictionary[k] >= 250:
                print(f"{k} obtained!")
    lines = input().split()
