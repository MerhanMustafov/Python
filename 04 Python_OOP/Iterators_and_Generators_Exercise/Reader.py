def read_next(*args):
    # cur = 0
    # while cur < len(args):
    #     for i in args[cur]:
    #         yield i
    #     cur += 1

    for seq in args:
        for el in seq:
            yield el
for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')



