class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        n = len(s)
        uniqueS = set()
        
        l, r = 0, 0
        maxSubstring = 0
        
        while r < n:
            while (s[r] in uniqueS):
                uniqueS.remove(s[l])
                l += 1
                
            uniqueS.add(s[r])
            maxSubstring = max(maxSubstring, r-l+1)
            r += 1
            
        return maxSubstring
            
            