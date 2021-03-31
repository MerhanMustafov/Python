input_lines = input()

data = {}
while not input_lines == "Season end":
    if "->" in input_lines:
        input_lines = input_lines.split(" -> ")
        player = input_lines[0]
        position = input_lines[1]
        skill = int(input_lines[2])
        if not player in data.keys():
            data[player] = {'p': [position], 's': [skill]}
        else:
            data[player]['p'].append(position)
            data[player]['s'].append(skill)
    elif "vs" in input_lines:
        input_lines = input_lines.split(" vs ")
        player_1 = input_lines[0]
        player_2 = input_lines[1]
        if player_1 in data and player_2 in data:
            if [i for i in data[player_1]['p']] == [x for x in data[player_2]['p']]:

                if sum(data[player_1]['s']) < sum(data[player_2]['s']):
                    del [player_1]
                elif sum(data[player_2]['s']) < sum(data[player_1]['s']):
                    del [player_2]
                else:
                    input_lines = input()
                    continue

    input_lines = input()
