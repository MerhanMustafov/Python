bunker = {category: [] for category in input().split(", ")}
n = int(input())
bunker['all_items_count'] = 0
bunker['all_quality'] = 0

for _ in range(n):
    category, item_name, item_params = input().split(" - ")
    item_quantity = int(item_params.split(';')[0].split(':')[1])
    item_quality = int(item_params.split(';')[1].split(':')[1])
    item_data = {item_name: {"quantity": item_quantity, 'quality': item_quality}}
    bunker[category].append(item_data)
    bunker['all_items_count'] += item_quantity
    bunker['all_quality'] += item_quality
print(f"Count of items: {bunker['all_items_count']}")
print(f"Average quality: {(bunker['all_quality']/(len(bunker)-2)):.2f}")

print(*[f"{category} -> {', '.join([list(d.keys())[0] for d in value])}" for category, value in bunker.items() if isinstance(bunker[category], list)], sep="\n")







# items_in_bunker = input().split(", ")
# n = int(input())
#
# # dictionary = {"food": {"item_name":"" {"quantity": 0, 'auality': 0}}}
# dictionary = {}
# dict_for_items = {}
# for _ in range (n):
#     category, item_name, quantity_quality = input().split("-")
#     quantity, quality = quantity_quality.split(";")
#     if not category in dictionary:
#         dictionary[category] = {"quantity": 0, 'quality': 0}
#     if not category in dict_for_items:
#         dict_for_items[category] = []
#     dict_for_items[category].append(item_name.strip())
#     quantity = quantity.split(":")
#     quality = quality.split(":")
#     dictionary[category]["quantity"] += int(quantity[1])
#     dictionary[category]["quality"] += int(quality[1])
#     # print(dictionary)
# count = 0
# average = 0
# for k, v in dictionary.items():
#     count += v["quantity"]
#     average += v["quality"]
#
#
# print(f"Count of items: {count}")
# average = average/((len(items_in_bunker)))
# print(f"Average quality: {average:.2f}")
#
# for key, value in dict_for_items.items():
#     key = key.strip()
#     print(f"{key} -> {', '.join(value)}")



