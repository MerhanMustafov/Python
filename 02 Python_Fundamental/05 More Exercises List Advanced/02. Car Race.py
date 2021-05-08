lst_numbers = input().split(" ")
lst_numbers = list(map(int, lst_numbers))
# print(lst_numbers)
first = len(lst_numbers) // 2
# print(first)
second = first
# print(second)
total_first = 0
total_second = 0
for left_car in range(0, first):
    if lst_numbers[left_car] == 0:
        total_first *= 0.8
    else:
        total_first += lst_numbers[left_car]
for right_car in range(len(lst_numbers) - 1, second, -1):
    if lst_numbers[right_car] == 0:
        total_second *= 0.8
    else:
        total_second += lst_numbers[right_car]

if total_first < total_second:
    print(f"The winner is left with total time: {total_first:.1f}")
elif total_first > total_second:
    print(f"The winner is right with total time: {total_second:.1f}")

