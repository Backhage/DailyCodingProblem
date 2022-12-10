import heapq


def regular_numbers(n):
    solution = [1]
    last = 0
    count = 0

    while count < n:
        x = heapq.heappop(solution)
        if x > last:
            yield x
            last = x
            count += 1
            heapq.heappush(solution, x * 2)
            heapq.heappush(solution, x * 3)
            heapq.heappush(solution, x * 5)
