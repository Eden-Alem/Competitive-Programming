def maximumToys(prices, k):
    prices.sort()
    count  = 0
    afford = 0
    for i in range(len(prices)):
        if ((count + prices[i]) < k):
            count += prices[i]
            afford += 1
    return afford