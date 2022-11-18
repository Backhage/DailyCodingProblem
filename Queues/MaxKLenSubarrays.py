from collections import deque


def max_of_subarrays(lst, k):
    q = deque()

    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

    result = []
    for i in range(k, len(lst)):
        result.append(lst[q[0]])

        while q and q[0] <= i - k:
            q.popleft()

        while q and lst[i] >= lst[q[-1]]:
            q.pop()

        q.append(i)

    result.append(lst[q[0]])
    return result
