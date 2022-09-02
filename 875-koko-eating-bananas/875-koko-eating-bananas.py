class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        best = right = max(piles)
        
        while left <= right:
            mid = (left+right) // 2
            
            if (self.kokosTime(piles, mid, h)):
                best = mid
                right = mid-1
            else:
                left = mid + 1
                
        return best
            
    def kokosTime(self, piles, s, h):
        time = 0
        for pile in piles:
            time += ceil(pile / s)
            
        return time <= h
        