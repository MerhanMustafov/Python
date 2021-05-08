n = int(input())
my_dict = {}
for _ in range(n):
    command = input().split("<->")
    plant = command[0]
    rarity = int(command[1])
    if not plant in my_dict.keys():
        my_dict[plant] = {'rarity': rarity, 'ratings': []}

new_command = input()
while not new_command == "Exhibition":
    new_command = new_command.split(": ")
    if new_command[0] == "Rate":
        r = new_command[1].split(" - ")
        plant = r[0]
        rating = int(r[1])
        if plant in my_dict:
            my_dict[plant]['ratings'].append(rating)
        else:
            print('error')
    elif new_command[0] == "Update":
        s = new_command[1].split(" - ")
        plant = s[0]
        new_rarity = int(s[1])
        if plant in my_dict:
            my_dict[plant]["rarity"] = new_rarity
        else:
            print('error')
    elif new_command[0] == "Reset":
        plant = new_command[1]
        if plant in my_dict:
            my_dict[plant]["ratings"].clear()
        else:
            print('error')
    else:
        print('error')
    new_command = input()
for plant,value  in my_dict.items():
    if value['ratings']:
        avg = sum(value['ratings']) / len(value['ratings'])
    else:
        avg = 0
    my_dict[plant]['avg'] = avg

my_dict_one = sorted(my_dict.items(), key=lambda x: (-x[1]['rarity'], -x[1]['avg']) )
print(f"Plants for the exhibition:")
for plant_name, values in my_dict_one:
    print(f"- {plant_name}; Rarity: {values['rarity']}; Rating: {values['avg']:.2f}")
