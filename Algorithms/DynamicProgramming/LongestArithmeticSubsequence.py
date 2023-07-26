def longest_arithmetic_subsequence(nums):
    lengths = {}

    for right in range(len(nums)):
        for left in range(right):
            diff = nums[right] - nums[left]
            lengths[(right, diff)] = lengths.get((left, diff), 1) + 1

    return max(lengths.values())
