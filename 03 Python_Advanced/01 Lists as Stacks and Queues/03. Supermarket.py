from collections import deque
command = input()
q = deque()


while not command == "End":
    if command == "Paid":
        while q:
            print(q.popleft())
        command = input()
        continue

    q.append(command)
    command = input()


print(f"{len(q)} people remaining.")


