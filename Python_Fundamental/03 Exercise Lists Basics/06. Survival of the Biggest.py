string = input()
lst = string.split(" ")
num_lst = list(map(int, lst))


n = int(input())
for i in range (n):
   num_lst.remove(min(num_lst))
print(num_lst)
