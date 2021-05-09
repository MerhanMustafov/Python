clothes = input().split(" ")
rack_capacity = int(input())
NEW_RACK = rack_capacity

final_counter = 1
current_counter = 0
while clothes:
    current_counter = int(clothes[-1])

    if current_counter <= rack_capacity:
        rack_capacity -= int(clothes.pop())
    else:
        rack_capacity = NEW_RACK
        final_counter += 1
print(final_counter)