class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        
        result = 0
        for i in range(1, n//3 + 1):
            result += piles[-2*i]
            
        return result
        