def exchange(nums_list, index):
    a = 5
    first_part = nums_list[index + 1:]
    second_part = nums_list[:index + 1]
    result = first_part + second_part
    return result
def find_max_min(num_list, odd_or_even):
    filterd_nums = []
    if odd_or_even:
        for el in num_list:
            if not el % 2 == 0:
                filterd_nums.append(el)
    else:
        for el in num_list:
            if el % 2 == 0:
                filterd_nums.append(el)
    max_elements = max(filterd_nums)
    if not filterd_nums:
        return "No matches"
    index = len(filterd_nums) - filterd_nums[::-1].index(filterd_nums)-1
    return index

def find_

nums_as_string = input().split()
num = []
for el in nums_as_string:
    num.append(int(el))

command_date = input()
while not command_date == "end":
    command_date = command_date.split()
    command = command_date[0]
    if command == "exchange":
        i = int(command_date[1])
        nums = exchange(nums, i)
    elif command == "max":
        odd_or_even = command_date[1]
        find_max_min(nums, odd_or_even)
    elif command == "min":
        pass
    elif command == "first":
        pass
    elif command == "last":
        pass

    command_date = input()


