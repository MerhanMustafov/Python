from collections import deque


def best_list_pureness(*test):
    k = test[-1]
    lst = deque(test[0])
    best_pureness = 0
    best_rotation_num = 0
    for x in range(k+1):
        best = sum([el * lst[el] for el in range(len(lst))])
        if best > best_pureness:
            best_pureness = best
            best_rotation_num = x
        lst.insert(0, lst.pop())
    return f"Best pureness {best_pureness} after {best_rotation_num} rotations"


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)
