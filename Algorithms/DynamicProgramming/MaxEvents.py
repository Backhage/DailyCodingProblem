import bisect


def max_value(events, k):
    # Sort the events by start day.
    events.sort()

    # Create a dp matrix for memoization, storing intermediate results.
    n = len(events)
    dp = [[None for _ in range(n)] for _ in range(k + 1)]

    # The start days list will be used for binary search for the next available event.
    start_days = [start_day for start_day, end_day, value in events]

    def dfs(current_index, count):
        if count == 0 or current_index == n:
            return 0

        if dp[count][current_index] is not None:
            return dp[count][current_index]

        # Find the nearest available event after attending the current event.
        current_end_day = events[current_index][1]
        next_index = bisect.bisect_right(start_days, current_end_day)

        # Set the entry in the dp matrix to the maximum of the two alternatives:
        # 1. Skip current event and attend the next instead.
        # 2. Attend current event and then the next possible after.
        current_value = events[current_index][2]
        dp[count][current_index] = max(
            dfs(current_index + 1, count),
            current_value + dfs(next_index, count - 1),
        )

        return dp[count][current_index]

    return dfs(0, k)
