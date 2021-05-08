legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
key_resources = {'motes': 0, 'shards': 0, 'fragments': 0}
junk_resources = {}
while True:
    is_reached = False
    line = input().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1].lower()
        if material in key_resources:
            key_resources[material] += quantity
            if key_resources[material] >= 250:
                print(f'{legendary_items[material]} obtained!')
                is_reached = True
                key_resources[material] -= 250
                break
        else:
            if material not in junk_resources:
                junk_resources[material] = 0
            junk_resources[material] += quantity
    if is_reached:
        break


ordered_key_materials = dict(sorted(key_resources.items(), key=lambda x: (-x[1], x[0])))
ordered_junk_materials = dict(sorted(junk_resources.items(), key=lambda x: (x[0])))


for key, value in ordered_key_materials.items():
    print(f'{key}: {value}')
for x, y in ordered_junk_materials.items():
    print(f'{x.lower()}: {y}')