from collections import deque


def int_to_str(n):
    return [str(x) for x in n]


def decreace_and_move(f_effect):
    f_effect[0] -= 1
    f_effect.append(f_effect.popleft())
    # return palm_firework, willow_firework, crossette_firework


def check_divisibility(f_effects, e_power, palm_firework, willow_firework, crossette_firework):

    if ((sum([f_effects[0], e_power[-1]]) % 3 == 0) and (sum([f_effects[0], e_power[-1]]) % 5 == 0)):
        f_effects.popleft(), e_power.pop()
        crossette_firework += 1
    elif ((sum([f_effects[0], e_power[-1]]) % 3 == 0) and (sum([f_effects[0], e_power[-1]]) % 5 != 0)):
        f_effects.popleft(), e_power.pop()
        palm_firework += 1
    elif ((sum([f_effects[0], e_power[-1]]) % 3 != 0) and (sum([f_effects[0], e_power[-1]]) % 5 == 0)):
        f_effects.popleft(), e_power.pop()
        willow_firework += 1

    else:
        decreace_and_move(f_effects)

    return palm_firework, willow_firework, crossette_firework


firework_effects = deque([int(n) for n in input().split(", ")])
explosive_power = deque([int(n) for n in input().split(", ")])

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while firework_effects and explosive_power:

    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    if (firework_effects[0] <= 0) and (explosive_power[-1] <= 0):
        firework_effects.popleft(), explosive_power.pop()
        continue
    else:
        palm_firework, \
        willow_firework, \
        crossette_firework = check_divisibility(firework_effects, explosive_power,
                                                palm_firework, willow_firework,
                                                crossette_firework)
        if ((palm_firework >= 3) and (willow_firework >= 3) and (crossette_firework >= 3)):
            break

if ((palm_firework >= 3) and (willow_firework >= 3) and (crossette_firework >= 3)):
    print(f"Congrats! You made the perfect firework show!")

else:
    print(f"Sorry. You can't make the perfect firework show.")


if firework_effects:
    print(f"Firework Effects left: {', '.join(int_to_str(firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(int_to_str(explosive_power))}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")
