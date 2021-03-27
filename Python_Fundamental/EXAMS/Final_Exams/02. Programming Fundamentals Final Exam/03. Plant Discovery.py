n = int(input())
my_dict = {}
for _ in range(n):
    command = input().split("<->")
    plant = command[0]
    rarity = int(command[1])
    if not plant in my_dict.keys():
        my_dict[plant] = {'Rarity': rarity, 'Rating': []}
    elif plant in my_dict.keys():
        my_dict[plant]['Rarity'] = rarity

new_command = input()
while not new_command == "Exhibition":
    new_command = new_command.split(": ")
    if new_command[0] == "Rate":
        r = new_command[1].split(" - ")
        plant = r[0]
        rating = int(r[1])
        my_dict[plant]['Rating'].append(rating)
    elif new_command[0] == "Update":
        s = new_command[1].split(" - ")
        plant = s[0]
        new_rarity = int(s[1])
        my_dict[plant]["Rarity"] = new_rarity
    elif new_command[0] == "Reset":
        plant = new_command[1]
        my_dict[plant]["Rating"] = [0.0]
    else:
        print('error')
    new_command = input()
for p,c  in my_dict.items():
    o = c['Rating']
    c['Rating'] = sum(o) / len(o)

my_dict = dict(sorted(my_dict.items(), key=lambda x: (x[0][2], x[0][3]), reverse=True))
print(f"Plants for the exhibition:")
for a, b in my_dict.items():
    print(f"- {a}; Rarity: {b['Rarity']}; Rating: {b['Rating']:.2f}")
