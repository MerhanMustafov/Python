lines = input()
data = {}
count = data.keys()
while not lines == "Statistics":
    lines = lines.split("->")
    if lines[0] == "Add":
        user_name = lines[1]
        if user_name not in data:
            data[user_name] = []
        else:
            print(f"{user_name} is already registered")
    elif lines[0] == "Send":
        user = lines[1]
        email = lines[2]
        data[user].append(email)
    elif lines[0] == "Delete":
        user_n = lines[1]
        if user_n in data.keys():
            data.pop(user_n)
        else:
            print(f"{user_n} not found!")
    data.keys()
    lines = input()
data = sorted(data.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

print(f"Users count: {len(count)}")
for k, v in data:
    print(k)
    for one in range(len(v)):
        print(f" - {v[one]}")

