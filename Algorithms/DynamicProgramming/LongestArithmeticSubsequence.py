def longest_arithmetic_subsequence(nums):
    dp = {}

    for right in range(len(nums)):
        for left in range(0, right):
            diff = nums[right] - nums[left]
            dp[(right, diff)] = dp.get((left, diff), 1) + 1

    return max(dp.values())
