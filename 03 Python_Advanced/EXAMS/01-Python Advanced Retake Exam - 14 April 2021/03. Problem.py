def flights(*args):
    dictionary = {}
    for n in range(0, len(args), 2):
        if args[n] == 'Finish':
            return dictionary
        elif args[n] not in dictionary:
            dictionary[args[n]] = int(args[n+1])
        else:
            dictionary[args[n]] += int(args[n+1])

# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))


