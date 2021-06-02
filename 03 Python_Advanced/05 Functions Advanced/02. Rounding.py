def round_iter_element(nums_list):
    result = [round(el) for el in nums_list]
    return result

nums = map(lambda el: float(el), input().split())
print(round_iter_element(nums))