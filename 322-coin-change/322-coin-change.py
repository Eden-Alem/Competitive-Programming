class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)      
        def numOfCoinsUsed(amount):
            if amount == 0:
                return 0
            
            minCoins = float("inf")
            for coin in coins:
                if (amount - coin) >= 0:
                    temp = numOfCoinsUsed(amount-coin)
                    if temp == -1: continue
                    minCoins = min(minCoins, 1 + temp)
                
            return minCoins if minCoins != float("inf") else -1
        
        return numOfCoinsUsed(amount)
            
        
#          1     2      5
#         1 2 5  1 2 5
        
#         decrease the amount till we reach 0 by the coins available
        
#         for the current calculated amount using the coins available, 
#         how many coins did you use?
        
#         Will take the minimum response from all
        
#         amount <= 0 - base case
#         if amount <= 0: return 0
        
#         states - amount
#         dp(amount)
        
#         min(rn)
        
        
        