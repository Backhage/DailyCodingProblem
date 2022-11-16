def maximum_circular_subarray(nums):
    max_wrap_around = sum(nums) - min_subarray_sum(nums)
    return max(max_subarray_sum(nums), max_wrap_around)


def min_subarray_sum(nums):
    min_ending_here = min_so_far = 0
    for num in nums:
        min_ending_here = min(num, min_ending_here + num)
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far


def max_subarray_sum(nums):
    max_ending_here = max_so_far = 0
    for num in nums:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
