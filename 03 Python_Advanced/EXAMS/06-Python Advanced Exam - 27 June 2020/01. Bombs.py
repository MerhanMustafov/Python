from collections import deque

def int_to_str(bombs):
    return [str(n) for n in bombs]
DATURA = 40
CHERRY = 60
SMOKE_DECOY = 120

bomb_effects = deque([int(n) for n in input().split(", ")])
bomb_casings = [int(n) for n in input().split(", ")]


bomb_counts = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
poch_filled = False
while bomb_effects and bomb_casings:

    if bomb_effects[0] + bomb_casings[-1] == DATURA:
        bomb_counts['Datura Bombs'] += 1
        bomb_effects.popleft(), bomb_casings.pop()
    elif bomb_effects[0] + bomb_casings[-1] == CHERRY:
        bomb_counts['Cherry Bombs'] += 1
        bomb_effects.popleft(), bomb_casings.pop()
    elif bomb_effects[0] + bomb_casings[-1] == SMOKE_DECOY:
        bomb_counts['Smoke Decoy Bombs'] += 1
        bomb_effects.popleft(), bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5
    if bomb_counts['Datura Bombs'] >= 3 and bomb_counts['Cherry Bombs'] >= 3 and bomb_counts['Smoke Decoy Bombs'] >= 3:
        poch_filled = True
        break


if poch_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(int_to_str(bomb_effects))}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(int_to_str(bomb_casings))}")
else:
    print("Bomb Casings: empty")

bomb_counts = sorted(bomb_counts.items(), key=lambda x: x[0])
for key, value in bomb_counts:
    print(f"{key}: {value}")