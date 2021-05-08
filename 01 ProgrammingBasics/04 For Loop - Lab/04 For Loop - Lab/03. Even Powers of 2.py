import math
n = int(input())
for power in range (1, n + 1 ):
    if power % 2 == 0:
        print(math.floor(math.pow(2, power)))

