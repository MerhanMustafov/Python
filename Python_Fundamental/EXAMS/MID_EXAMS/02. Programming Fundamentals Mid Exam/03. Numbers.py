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