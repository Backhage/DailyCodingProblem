import heapq


def get_median(min_heap, max_heap):
    if len(min_heap) > len(max_heap):
        return min_heap[0]
    elif len(max_heap) > len(min_heap):
        return -1 * max_heap[0]
    else:
        return (min_heap[0] + -1 * max_heap[0]) / 2.0


def add_number(num, min_heap, max_heap):
    if len(min_heap) == len(max_heap) == 0:
        heapq.heappush(min_heap, num)
        return

    median = get_median(min_heap, max_heap)
    if num >= median:
        heapq.heappush(min_heap, num)
    else:
        heapq.heappush(max_heap, -1 * num)


def rebalance(min_heap, max_heap):
    if len(min_heap) > len(max_heap) + 1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -1 * root)
    elif len(max_heap) > len(min_heap) + 1:
        root = -1 * heapq.heappop(max_heap)
        heapq.heappush(min_heap, root)


def running_median(stream):
    min_heap = []
    max_heap = []
    running_median = []

    for num in stream:
        add_number(num, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        running_median.append(get_median(min_heap, max_heap))

    return running_median
