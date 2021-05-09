numbers = input().split()
new_numbers = []
while numbers:
    new_numbers.append(numbers.pop())

# print(*new_numbers, sep=" ")
print(" ".join(new_numbers))


# numbers = input().split()
# new_numbers = ''
# while numbers:
#     new_numbers += numbers.pop() + ' '
#
# print(new_numbers)