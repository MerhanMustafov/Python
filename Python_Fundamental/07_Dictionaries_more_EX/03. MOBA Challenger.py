input_lines = input()

data = {}
data_2 = {}
while not input_lines == "Season end":
    if "->" in input_lines:
        input_lines = input_lines.split(" -> ")
        player = input_lines[0]
        position = input_lines[1]
        skill = int(input_lines[2])
        if not player in data.keys():
            data[player] = {'p': [position], 's': [skill]}
            data_2[player] = {'p': position, 's': skill}

        else:
            data[player]['p'].append(position)
            data[player]['s'].append(skill)
            data_2[player]['s'] += skill
    elif "vs" in input_lines:
        input_lines = input_lines.split(" vs ")
        player_1 = input_lines[0]
        player_2 = input_lines[1]
        if player_1 in data and player_2 in data:
            for x in data[player_1]['p']:
                for y in data[player_2]['p']:
                    if x == y:
                        if sum(data[player_1]['s']) < sum(data[player_2]['s']):
                            data.pop(player_1)
                        elif sum(data[player_2]['s']) < sum(data[player_1]['s']):
                            data.pop(player_2)
                        else:
                            input_lines = input()
                            continue

    input_lines = input()

data = sorted(data.items(), key=lambda kdv: (-sum(kdv[1]['s']), kdv[0]))
for key, dict in data:
    print(f"{key}: {sum(dict['s'])} skill")
    dict['s'].sort(reverse= True)
    dict['p'].sort(reverse = True)
    for x in sorted(dict['s']):
        dict['s'].sort()
    # for k, v in sorted(data[]):
        print(dict)
        a = 0