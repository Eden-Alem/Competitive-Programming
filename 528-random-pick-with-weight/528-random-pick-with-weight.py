class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        
        for weight in w:
            total += weight
            
            self.prefix.append(total)
            
        self.total = total
        

    def pickIndex(self) -> int:
        rand_num = random.uniform(0, self.total)
        
        l, r = 0, len(self.prefix)
        
        while l < r:
            mid = l + (r - l) // 2
            if self.prefix[mid] < rand_num:
                l = mid + 1
            else:
                r = mid 
                
        return l 
                
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()