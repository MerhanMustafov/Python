rooms = int(input())
count_free = 0

for room in range(rooms):
    current_room = input()
    chairs, taken = current_room.split(" ")
    chairs = len(list(map(str, chairs)))
    if chairs >= int(taken):
        count_free += chairs - int(taken)
    else:
        print(f"{abs(chairs - int(taken))} more chairs needed in room {room+1}")
        count_free -= abs(chairs - int(taken))

if count_free >= 0:
    print(f"Game On, {count_free} free chairs left")