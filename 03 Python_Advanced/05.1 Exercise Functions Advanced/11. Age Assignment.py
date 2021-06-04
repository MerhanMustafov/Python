def age_assignment(*args, **kwargs):
    dictionary = {}
    for el in range(len(args)):
        dictionary[args[el]] = None
    for letter, ageee in kwargs.items():
        for k, v in dictionary.items():
            if k[0] == letter:
                dictionary[k] = ageee
        # if any(letter == dictionary):
        #     dictionary[letter] = ageee
    return dictionary
# tupleee = (name for name in input().split(", "))
# dict = {k: k[1] for k in input().split("=")}
#
# print(age_assignment(tupleee, dict))
