def shifted_array_search(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            return mid

        if array[low] <= array[mid]:
            if array[low] <= target <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if array[mid] <= target <= array[high]:
                low = mid + 1
            else:
                high = mid - 1

    return None
