import random
lst1 = input()
lst1 = lst1.split()
start = str(lst1[0])
end = str(lst1[-1])
s = []
s.append(start)
e = []
e.append(end)
lst1 = lst1[1:-1]
n = int(input())
for time in range(n):

    random.shuffle(lst1)
print(s + lst1 + e )