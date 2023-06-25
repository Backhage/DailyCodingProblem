def max_profit(prices, fee):
    n = len(prices)
    hold, free = -prices[0], 0

    for i in range(1, n):
        tmp = hold
        hold = max(hold, free - prices[i])
        free = max(free, tmp + prices[i] - fee)

    return free
