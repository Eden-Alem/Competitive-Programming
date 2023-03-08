class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        
        l, r = 0, 0
        unique = set()
        count = 1
        while r < n:
            if s[r] in unique:                
                unique = set()
                count += 1
                l = r
                
            unique.add(s[r])
                
            r += 1
            
        return count
        