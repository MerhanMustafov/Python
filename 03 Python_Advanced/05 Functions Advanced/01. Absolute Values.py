def convert_to_abs_value(num_list):
    return list(map(lambda x: abs(x), num_list))
nums = map(lambda el: float(el), input().split())
print(convert_to_abs_value(nums))

# def convert_to_abs_value(num_list):
#     return [abs(num) for num in num_list]
#
# nums = [float(n) for n in input().split()]
# result = convert_to_abs_value(nums)
# print(result)

