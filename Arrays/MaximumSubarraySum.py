def max_subarray_sum(nums):
    max_so_far = max_ending_here = 0
    for num in nums:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
