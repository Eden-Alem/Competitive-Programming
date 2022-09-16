class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        
        for amt in range(1, amount+1):
            for coin in coins:
                if (amt - coin) >= 0:
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        
        return dp[-1] if dp[-1] != float("inf") else -1
            
        
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
        
        
        