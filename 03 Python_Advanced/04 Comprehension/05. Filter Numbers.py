start = int(input())
stop = int(input())
def is_valid(x):
    return any(x % i == 0 for i in range(2, 11))

print(
    [x for x in range(start, stop+1) if is_valid(x) ]
)