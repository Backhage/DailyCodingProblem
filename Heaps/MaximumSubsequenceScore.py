import heapq


def max_score(nums1, nums2, k):
    pairs = [(a, b) for a, b in zip(nums1, nums2)]
    pairs.sort(key=lambda x: -x[1])

    top_k_heap = [x[0] for x in pairs[:k]]
    heapq.heapify(top_k_heap)

    top_k_sum = sum(top_k_heap)
    answer = top_k_sum * pairs[k - 1][1]

    for pair in pairs[k:]:
        top_k_sum -= heapq.heappop(top_k_heap)
        top_k_sum += pair[0]
        heapq.heappush(top_k_heap, pair[0])

        answer = max(answer, top_k_sum * pair[1])

    return answer
