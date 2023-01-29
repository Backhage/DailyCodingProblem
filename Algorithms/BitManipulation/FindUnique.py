# Find an element that only appear once while all others appear three times.
def find_unique(arr):
    result_arr = [0] * 32
    for num in arr:
        for i in range(32):
            bit = num >> i & 1
            result_arr[i] += bit

    result = 0
    for i, bit in enumerate(result_arr):
        if bit % 3 != 0:
            result += 2**i

    # Also cover for negative integers
    return result if result < (1 << 31) else result - (1 << 32)
