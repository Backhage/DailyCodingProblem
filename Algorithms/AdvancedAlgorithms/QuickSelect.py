def find_kth_largest(nums, k):
    # Change k to be the index where the k:th largest value
    # will be saved when doing the quick select.
    k = len(nums) - k

    def quick_select(left, right):
        pivot, p = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        nums[p], nums[right] = nums[right], nums[p]

        if p > k:
            return quick_select(left, p - 1)
        elif p < k:
            return quick_select(p + 1, right)
        else:
            return nums[p]

    return quick_select(0, len(nums) - 1)
