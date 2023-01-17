def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def pancake_sort(arr):
    for i in reversed(range(len(arr))):
        max_idx = arr.index(max(arr[: i + 1]))
        reverse(arr, 0, max_idx)
        reverse(arr, 0, i)
