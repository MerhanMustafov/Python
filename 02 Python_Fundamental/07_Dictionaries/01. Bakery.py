elements = input().split()
bakery = {}
for el in range(0, len(elements), 2):
    key = elements[el]
    value = int(elements[el + 1])
    bakery[key] = value
print(bakery)