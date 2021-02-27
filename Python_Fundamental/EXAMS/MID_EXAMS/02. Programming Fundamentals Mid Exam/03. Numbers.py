sequence_of_int = list(map(int, input().split()))
sum_of_sq = sum(sequence_of_int)
average = sum_of_sq // len(sequence_of_int)

final = [num for num in sequence_of_int if num > average]

if len(final) == 0:
    print("No")
else:
    final.sort(reverse=True)
    final = final[:5]
print(*final, sep=" ")

# numbers = [int(x) for x in input().split()]
# average = sum(numbers) / len(numbers)
# numbers = [num for num in numbers if num > average]
# if all(x==numbers for x in numbers):
#     print("No")
# else:
#     numbers.sort(reverse=True)
#     print(*numbers[:5],sep=" ")