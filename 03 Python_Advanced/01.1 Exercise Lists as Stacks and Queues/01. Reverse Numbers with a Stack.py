numbers = input().split()

stack = []
while numbers:
    stack.append(numbers.pop())

# print(*new_numbers, sep=" ")
print(" ".join(stack))

#1st solution
# new_num = [int(n) for n in reversed(numbers)]
# print(*new_num, sep=" ")

# 2nd solution
# numbers = input().split()
# new_numbers = ''
# while numbers:
#     new_numbers += numbers.pop() + ' '
#
# print(new_numbers)