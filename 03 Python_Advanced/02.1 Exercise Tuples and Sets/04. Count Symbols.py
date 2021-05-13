def creating_dictionary(s):
    dictionary = {}
    for symbol in string:
        dictionary[symbol] = string.count(symbol)
    return dictionary


string = input()
dictionary = creating_dictionary(string)
dictionary = sorted(dictionary.items(), key=lambda kvp: kvp[0])
for k, v in dictionary:
    print(f"{k}: {v} time/s")

# from collections import deque
# string = deque(input())
# dictionary = {}
# for symbol in string:
#     dictionary[symbol] = string.count(symbol)
# dictionary = sorted(dictionary.items(), key=lambda kvp: kvp[0])
# for k, v in dictionary:
#     print(f"{k}: {v} time/s")