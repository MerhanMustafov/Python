def collecting_numbers(n):
    nums = []
    for _ in range(n):
        nums.append(input())
    return nums
numbers = input().split(" ")
n = int(numbers[0])
m = int(numbers[1])

lst_1 = set(collecting_numbers(n))
lst_2 = set(collecting_numbers(m))
for num in lst_1:
    if num in lst_2:
        print(num)


# numbers = input().split(" ")
# n = int(numbers[0])
# m = int(numbers[1])
#
# lst_1 = []
# for _ in range(n):
#     num = int(input())
#     lst_1.append(num)
#
# lst_2 = []
# for _ in range(m):
#     num_2 = int(input())
#     lst_2.append(num_2)
#
# lst_1 = set(lst_1)
# lst_2 = set(lst_2)
# repeatint_onece = []
# for nummmm in lst_1:
#     if nummmm in lst_2:
#         repeatint_onece.append(nummmm)
# for nber in repeatint_onece:
#     print(nber)