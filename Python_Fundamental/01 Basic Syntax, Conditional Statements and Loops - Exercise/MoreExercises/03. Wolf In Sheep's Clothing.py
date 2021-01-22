animals = input()
animals_list = animals.split(sep=', ')
if animals_list[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for idx, animal in enumerate(animals_list):
        if animal == 'wolf':
            print(
                f'Oi! Sheep number {len(animals_list)-idx-1}! You are about to be eaten by a wolf!')
            break
# herd = [item for item in input().split(", ")]
# # herd = input().split(", ")
# if herd[-1] == "wolf":
#     print("Please go away and stop eating my sheep")
# else:
#     herd = herd[herd.index("wolf") + 1:]
#     print(f"Oi! Sheep number {len(herd)}! You are about to be eaten by a wolf!")