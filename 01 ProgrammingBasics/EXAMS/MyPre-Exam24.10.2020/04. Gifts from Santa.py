# •	N – цяло число – 0 <= N < M
# •	M – цяло число – N < M <= 10000
# •	S – цяло числo – N <= S <= M
import sys

n = int(input())
m = int(input())
s = int(input())

for number in range(m, n-1, -1):
    if number % 2 == 0 and number % 3 == 0:
        if number == s:
            sys.exit(0)
        else:
            print(number, end=' ')
