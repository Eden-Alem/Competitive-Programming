class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1000000007
        
        memo = {}
        def count(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            if n in memo:
                return memo[n]
            
            memo[n] = (count(n-zero) + count(n-one)) % MOD
            
            return memo[n] % MOD
        
        result = 0
        for i in range(low, high+1):
            result += (count(i) % MOD)
            
        return result % MOD
        