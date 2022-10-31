class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxPrice = prices[n-1]
        maxProfit = 0
        
        for i in range(n-2,-1,-1):
            maxPrice = max(maxPrice, prices[i])
            maxProfit = max(maxProfit, maxPrice - prices[i])
            
        return maxProfit