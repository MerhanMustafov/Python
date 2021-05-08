data = input()
pool = {}
while not data == "Season end":
    if '->' in data:
        player, position, skill = data.split(' -> ')
        skill = int(skill)
        if player not in pool:
            pool[player] = {}
            pool[player][position] = skill
        elif player in pool and position not in pool[player]:
            pool[player][position] = skill
        elif player in pool and position in pool[player]:
            if pool[player][position] < skill:
                pool[player][position] = skill
    elif 'vs' in data:
        player_one, player_two = data.split(' vs ')
        if player_one in pool and player_two in pool:
            for el in pool[player_one]:
                if el in pool[player_two]:
                    if pool[player_one][el] > pool[player_two][el]:
                        pool.pop(player_two)
                    elif pool[player_one][el] < pool[player_two][el]:
                        pool.pop(player_one)
                    break


    data = input()
for k, v in pool.items():
    sum = 0
    for el in v:
        sum  += v[el]
    pool[k]['total'] = sum

s_pool = sorted(pool.items(), key=lambda kvp: (-kvp[1]['total'], kvp[0]))
for el in s_pool:
    print(f"{el[0]}: {el[1]['total']} skill")
    el[1].pop('total')
    s_skills = sorted(el[1].items(), key=lambda kvp: (-kvp[1], kvp[0]))
    for skill in s_skills:
        print(f"- {skill[0]} <::> {skill[1]}")