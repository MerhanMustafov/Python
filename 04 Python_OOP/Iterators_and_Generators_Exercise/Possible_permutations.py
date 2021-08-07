import itertools
def possible_permutations(elements):
    permutations = list(itertools.permutations(elements))
    for el in permutations:
        yield list(el)
    #
    # if len(elements) <= 1:
    #     yield elements
    # else:
    #     for perm in possible_permutations(elements[1:]):
    #         for i in range(len(elements)):
    #             # nb elements[0:1] works in both string and list contexts
    #             yield  perm[:i] + elements[0:1] + perm[i:]




[print(n) for n in possible_permutations([1, 2, 3])]