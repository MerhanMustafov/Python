command = input()
user_data = {}
is_in = False
while not command == "Lumpawaroo":
    if "|" in command:
        side, user = command.split(" | ")
        if not side in user_data:
            user_data[side] = []
        if not user in user_data[side]:
            user_data[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")
        for key, value in user_data.items():
            if user in user_data[key]:
                is_in = True
                break
        if is_in:
            for k, v in user_data.items():
                if k == side:
                    user_data[k].append(user)
                else:
                    user_data[k].remove(user)
                print(f"{user} joins the {k} side!")
        else:
            user_data[side].append(user)
            print(f"{user} joins the {side} side!")



    command = input()
user_data = sorted(user_data.items(),key=lambda kvp: (-len(kvp[1]), kvp[0]))
for k, v in user_data:
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        for n in sorted(v):
            print(f"! {n}")

