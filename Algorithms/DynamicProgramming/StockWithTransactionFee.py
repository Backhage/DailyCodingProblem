def max_profit(prices, fee):
    hold, free = -prices[0], 0

    for price in prices[1:]:
        tmp = hold
        hold = max(hold, free - price)
        free = max(free, tmp + price - fee)

    return free
