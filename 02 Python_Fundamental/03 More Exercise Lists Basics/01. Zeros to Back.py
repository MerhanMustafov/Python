numbers = input().split(", ")
numbers = [int(i) for i in numbers]

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] == 0:
        numbers.pop(i)
        numbers.append(0)
print(numbers)
# print(numbers.pop(4))
# print(numbers)