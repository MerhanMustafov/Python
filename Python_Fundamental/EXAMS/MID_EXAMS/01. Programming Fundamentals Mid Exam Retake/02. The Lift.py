queue = int(input())
wagon = list(map(int, input().split()))

position = 0
while queue > 0:
    if wagon[-1] == 4 and len(wagon) == position:
        break
    elif wagon[position] == 4:
        position += 1
        continue
    elif 0 <= queue < 4:
        for p in range(queue):
            wagon[position] += 1
            queue -= 1
        continue

    queue -= (4 - wagon[position])
    wagon[position] = 4
    position += 1

empty_spots = wagon.count(4)

if  empty_spots < len(wagon) and queue == 0:
    print("The lift has empty spots!")
elif empty_spots == len(wagon) and queue > 0:
    print(f"There isn't enough space! {queue} people in a queue!")
print(*wagon, sep=" ")
