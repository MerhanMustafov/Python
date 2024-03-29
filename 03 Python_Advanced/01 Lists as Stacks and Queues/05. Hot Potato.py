from collections import deque
players = input().split(" ")
steps = int(input())


q = deque(players)

counter = 0

while len(q) > 1:
    for _ in range(steps -1):
        q.append(q.popleft())
    print(f"Removed {q.popleft()}")
print(f"Last is {q.popleft()}")

# WITH .rotate()
# from collections import deque
#
# children = deque(input().split())
# count = int(input())
#
# while len(children) > 1:
#     children.rotate(-count)
#     print(f"Removed {children.pop()}")
#
# print(f"Last is {children.pop()}")




# players = input().split(" ")
# steps = int(input())
#
#
# q = deque(players)
#
# counter = 0
#
# while len(q) > 1:
#     counter += 1
#     current_player = q.popleft()
#     if counter == steps:
#         print(f"Removed {current_player}")
#         counter = 0
#     else:
#         q.append(current_player)
#
# print(f"Last is {q.popleft()}")