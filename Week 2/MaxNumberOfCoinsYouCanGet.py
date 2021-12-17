class Solution:
    def maxCoins(self, piles) -> int:
        piles.sort()
        
        result = 0
        for i in range(1,len(piles)//3 + 1):
            result += piles[i*-2]
            
        return result
        