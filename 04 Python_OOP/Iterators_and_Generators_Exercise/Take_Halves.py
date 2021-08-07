def solution():
    def integers():
        nums = 1
        while True:
            yield nums + 1

    # TODO: Implement

    def halves():
        nums = []
        for i in integers():
            x = i/2
            nums.append(x)
        return nums

    # TODO: Implement

    def take(n, seq):
        lst = []
        for n in seq:
            lst.append(n)
    # TODO: Implement

    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
