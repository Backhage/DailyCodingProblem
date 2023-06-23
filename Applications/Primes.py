import heapq


def primes_less_than(n):
    is_prime = [False] * 2 + [True] * (n - 1)

    for x in range(2, int(n**0.5) + 1):
        if is_prime[x]:
            for i in range(x**2, n, x):
                is_prime[i] = False

    for i in range(n):
        if is_prime[i]:
            yield i


def primes():
    composite = []
    i = 2

    while True:
        # Note that composite[0][0] is the min element of the heap
        if composite and i == composite[0][0]:
            while composite[0][0] == i:
                multiple, p = heapq.heappop(composite)
                heapq.heappush(composite, [multiple + p, p])
        else:
            heapq.heappush(composite, [i * i, i])
            yield i

        i += 1
