vesues = tuple(map(float, input().split()))

velues_count = {}

for velue in vesues:
    if velue not in velues_count:
        velues_count[velue] = 0
    velues_count[velue] += 1
for key, v in velues_count.items():
    print(f"{key} - {v} times")

# vesues = tuple(map(float, input().split()))
# #
# # velues_count = {}
# #
# # for velue in vesues:
# #     velues_count[velue] = vesues.count(velue)
# # for key, v in velues_count.items():
# #     print(f"{key} - {v} times")
