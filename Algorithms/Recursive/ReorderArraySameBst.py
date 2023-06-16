import math


def number_of_ways(nums):
    mod = 10**9 + 7

    def dfs(nums):
        m = len(nums)
        if m < 3:
            return 1

        root = nums[0]
        left_nodes = [n for n in nums if n < root]
        right_nodes = [n for n in nums if n > root]

        return (
            dfs(left_nodes) * dfs(right_nodes) * math.comb(m - 1, len(left_nodes)) % mod
        )

    return (dfs(nums) - 1) % mod
