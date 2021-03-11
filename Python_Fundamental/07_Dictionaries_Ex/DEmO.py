sides = {}
command = input()
while command != 'Lumpawaroo':
    if '|' in command:
        side, user = command.split(' | ')
        if side not in sides:
            sides[side] = []
        if user not in sides[side]:
            sides[side].append(user)
        else:
            command=input()
            continue
    elif '->' in command:
        user, side = command.split(' -> ')
        for key, value in sides.items():
            if user in value:
                value.remove(user)
        if side not in sides:
            sides[side] = [user]
        elif user not in sides[side]:
            sides[side].append(user)
            print(f'{user} joins the {side} side!')
        else:
            command = input()
            continue
    command = input()
sorted_sides = sorted(sides.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
for key, value in sorted_sides:
    if len(value)>0:
        print(f'Side: {key}, Members: {len(value)}')
        sorted_values = sorted(value)
        for el in sorted_values:
            print(f'! {el}')