def concatenate(*args):
    result = list(map(str, (word+"" for word in args)))
    return result
    # string = ''
    # for word in args:
    #     string += word
    # return string
print(concatenate("Soft", "Uni", "Is", "Great", "!"))
