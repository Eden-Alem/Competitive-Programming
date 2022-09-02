class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        best = right = sum(weights)
        
        while left <= right:
            mid = (left + right) // 2
            
            if(self.canShip(weights, mid, days)):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return best
            
    def canShip(self, weights, w, days):
        d = 0
        i = 0
        
        s = 0
        while i < len(weights):
            if (s + weights[i] <= w):
                s += weights[i]
            else:
                d += 1
                s = weights[i]
                if s > w:
                    return False
                
            i += 1
            
        return d+1 <= days