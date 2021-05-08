houses = [int(x) for x in input().split("@")]

command = input()
cur_pos = 0
while not command == "Love!":
    jump, length = command.split()
    length = int(length)

    cur_pos += length
    if cur_pos >= len(houses):
        cur_pos = 0
    if houses[cur_pos] == 0:
        print(f"Place {cur_pos} already had Valentine's day.")
        command = input()
        continue
    houses[cur_pos] -= 2
    if houses[cur_pos] == 0:
        print(f"Place {cur_pos} has Valentine's day." )

    command = input()
print(f"Cupid's last position was {cur_pos}.")
if houses.count(0) == len(houses):
    print("Mission was successful.")
else:
    count = 0
    for x in houses:
        if x > 0:
            count += 1
    print(f"Cupid has failed {count} places.")