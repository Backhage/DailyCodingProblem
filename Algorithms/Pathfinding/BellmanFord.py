# Uses Bellman-Ford algorithm
def find_cheapest_price(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0

    for _ in range(k + 1):
        prices_copy = prices.copy()

        for source, dest, price in flights:
            if prices[source] + price < prices_copy[dest]:
                prices_copy[dest] = prices[source] + price

        prices = prices_copy

    return None if prices[dst] == float("inf") else prices[dst]
