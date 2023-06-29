import heapq


def max_score(nums1, nums2, k):
    pairs = [(a, b) for a, b in zip(nums1, nums2)]
    pairs.sort(key=lambda x: -x[1])

    top_k_heap = [x[0] for x in pairs[:k]]
    heapq.heapify(top_k_heap)

    top_k_sum = sum(top_k_heap)
    answer = top_k_sum * pairs[k - 1][1]

    for n1, n2 in pairs[k:]:
        top_k_sum -= heapq.heappop(top_k_heap)
        top_k_sum += n1
        heapq.heappush(top_k_heap, n1)

        answer = max(answer, top_k_sum * n2)

    return answer
