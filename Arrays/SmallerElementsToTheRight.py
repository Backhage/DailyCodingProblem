import bisect


def smaller_count(nums):
    result = []
    seen = []

    for num in reversed(nums):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort(seen, num)

    return list(reversed(result))
