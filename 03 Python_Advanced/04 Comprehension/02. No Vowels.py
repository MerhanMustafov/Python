vowels = {"a", "o", "u", "e", "i"}
# [vowels.add(x.upper()) for x in list(vowels)]
vowels = vowels.union(x.upper() for x in vowels)
string = [letter for letter in input() if not letter in vowels]
print(*string, sep="")