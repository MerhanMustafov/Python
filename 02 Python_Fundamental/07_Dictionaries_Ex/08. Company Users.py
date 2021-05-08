command = input()
data = {}
while not command == "End":
    command = command.split(" -> ")
    company_name = command[0]
    id = command[1]
    if company_name not in data:
        data[company_name] = []
    if not id in data[company_name]:
        data[company_name].append(id)
    command = input()
data = dict(sorted(data.items(), key=lambda kvp: kvp[0]))
for company, person in data.items():
    print(f"{company}")
    for p in data[company]:
        print(f"-- {p}")