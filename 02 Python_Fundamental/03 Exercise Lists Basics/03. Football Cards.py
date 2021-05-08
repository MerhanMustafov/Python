cards = input()
team_A = 11
team_B = 11
terminated = False
lst_cards = cards.split()
check_lst = []
for x in (lst_cards):
    if "A" in x:
        if x in check_lst:
            continue
        team_A -= 1
    elif "B" in x:
        if x in check_lst:
            continue
        team_B -= 1
    if team_A < 7 or team_B < 7:
        terminated = True
        break
    check_lst.append(x)
print(f"Team A - {team_A}; Team B - {team_B}")
if terminated:
    print(f"Game was terminated")