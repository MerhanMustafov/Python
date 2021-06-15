from collections import Counter


def numbers_searching(*nums):
    duplicates = sorted([item for item, count in Counter(nums).items() if count > 1])
    min_num = min(nums)
    max_num = max(nums)
    nums = sorted(set(nums))
    last_num = nums[0]

    for i in range(1, len(nums)):
        if nums[i] - last_num > 1:
            return [nums[i] - 1, duplicates]
        last_num = nums[i]
