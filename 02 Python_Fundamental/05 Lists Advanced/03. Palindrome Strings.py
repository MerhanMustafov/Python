words = input().split()
searched_palindrom = input()

all_palindromes = [word for word in words if word == word[::-1]]
print(all_palindromes)
print(f"Found palindrome {words.count(searched_palindrom)}")