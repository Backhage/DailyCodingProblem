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

        # Recursively call dfs on the left nodes and the right nodes to calculate
        # the ways to reorder them.
        # Also, the result needs to be multiplied by the binomial coefficient, which
        # represents the number of ways to reorder the elements without altering the
        # relative order of the nodes.
        binomial = math.comb(
            m - 1, len(left_nodes)
        )  # m - 1 since the root must stay in place
        return dfs(left_nodes) * dfs(right_nodes) * binomial % mod

    return (dfs(nums) - 1) % mod
