names = {name: {"items": [], "cost": 0}for name in input().split(", ")}

def final_dictionary(names):
    command = input()
    while not command == "End":
        name, item, cost = command.split("-")
        cost = int(cost)
        if not item in names[name]["items"]:
            names[name]["items"].append(item)
            names[name]["cost"] += cost
        command = input()
    return names

result = final_dictionary(names)
[print(f"{k} -> Items: {len(result[k]['items'])}, Cost: {result[k]['cost']}")for k, v in result.items()]
