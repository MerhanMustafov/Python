items_in_bunker = input().split(", ")
n = int(input())

# dictionary = {"food": {"item_name":"" {"quantity": 0, 'auality': 0}}}
dictionary = {}
dict_for_items = {}
for _ in range (n):
    category, item_name, quantity_quality = input().split(" - ")
    quantity, quality = quantity_quality.split(";")
    if not category in dictionary:
        dictionary[category] = {"quantity": 0, 'quality': 0}
    if not category in dict_for_items:
        dict_for_items[category] = []
    dict_for_items[category].append(item_name)
    quantity = quantity.split(":")
    quality = quality.split(":")
    dictionary[category]["quantity"] += int(quantity[1])
    dictionary[category]["quality"] += int(quality[1])
    # print(dictionary)
count = 0
average = 0
for k, v in dictionary.items():
    count += v["quantity"]
    average += v["quality"]


print(f"Count of items: {count}")
average = average/len(items_in_bunker)
print(f"Average quality: {average:.2f}")

for key, value in dict_for_items.items():
    print(f"{key} -> {', '.join(value)}")