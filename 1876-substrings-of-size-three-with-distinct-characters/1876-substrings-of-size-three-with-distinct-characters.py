class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        
        l, r = 0, 0
        size_3 = []
        
        while r < n:
            cur_len = r - l + 1
            
            while cur_len > 3:
                l += 1
                cur_len -= 1
                
            if cur_len == 3:
                size_3.append(s[l:r+1])
                
            r += 1
            
            
        count = 0
        for string in size_3:
            if self.isDistinct(string):
                count += 1
                
        return count
        
    def isDistinct(self, s):
        return len(set(s)) == len(s)
        
        