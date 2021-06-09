from collections import deque

def int_to_str(lst):
    return [str(x) for x in lst]

def check_for_matches(males,females, matches):
    matches = 0
    if males[-1] <= 0:
        males.pop()

    elif females[0] <= 0:
        females.popleft()

    elif males[-1] % 25 == 0:
        # males = males[0:len(males)-2] THIS DOES NOT WORK (it gives 92/100 wit runTimeError)
        males.pop(), males.pop()

    elif females[0] % 25 == 0:
        # females = females[2:] THIS DOES NOT WORK (it gives 92/100 wit runTimeError)
        females.popleft(), females.popleft()

    elif males[-1] == females[0]:
        matches += 1
        males.pop(), females.popleft()
    elif males[-1] != females[0]:
        females.popleft()
        males[-1] -= 2
    return matches


males = [int(n) for n in input().split()]
females = deque([int(n) for n in input().split()])
matches = 0
while males and females:

    matches += check_for_matches(males,females, matches)


print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(int_to_str(males)[::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(int_to_str(females))}")
else:
    print("Females left: none")