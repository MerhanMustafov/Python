vowels = ["a", "o", "u", "e", "i"]
string = [letter for letter in input() if not letter in vowels]
print(*string, sep="")