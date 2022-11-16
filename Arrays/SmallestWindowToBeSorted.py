def window(nums):
    max_seen, min_seen = -float("inf"), float("inf")
    left, right = None, None
    n = len(nums)

    for i in range(n):
        max_seen = max(max_seen, nums[i])
        if nums[i] < max_seen:
            right = i

    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, nums[i])
        if nums[i] > min_seen:
            left = i

    return (left, right)
