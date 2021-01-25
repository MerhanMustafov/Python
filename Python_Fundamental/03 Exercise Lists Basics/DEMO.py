# import random
# lst1 = [1, 2, 3, 4, 5, 6]
# start = str(lst1[0])
# start1 = list(map(str, start))
# end = str(lst1[-1])
# end2 = list(map(str, end))
# lst1 = lst1[1:-1]
# random.shuffle(lst1)
# print(start1 + lst1 + end2 )

mylist = [1,2,3,4,5,6]
slice = mutableslice(mylist, 2)
import random
random.shuffle(slice)
print(mylist)