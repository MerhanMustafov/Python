lst = list(map(int, input().split()))

command = input()

current_target = 0
while not command == "End":
    index = int(command)
    if index < len(lst):
        current_target = lst[index]
        lst[index] = -1
        for num in range(len(lst)):
            if not lst[num] == -1:
                if lst[num] > current_target:
                    lst[num] -= current_target
                else:
                    lst[num] += current_target
    command = input()
lst = list(map(str, lst))
print(f"Shot targets: {lst.count('-1')} -> {' '.join(lst)}")