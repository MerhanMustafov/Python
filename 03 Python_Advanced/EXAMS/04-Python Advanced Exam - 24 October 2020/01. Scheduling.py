from collections import deque

initial_nums = [int(el) for el in input().split(", ")]
index = int(input())

number = initial_nums[index]

initial_nums = [int(n) for n in initial_nums if n <= number]
print(sum(initial_nums))

