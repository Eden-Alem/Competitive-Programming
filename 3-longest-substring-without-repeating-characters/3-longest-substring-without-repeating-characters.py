class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        n = len(s)
        maxSubstring = 0
        l, r = 0, 0
        
        tempS = {}
        while r < n:
            if s[r] in tempS.keys():
                maxSubstring = max(maxSubstring, r-l)
                l = r = tempS[s[r]]+1
                tempS = {}
                
            tempS[s[r]] = r
            r += 1
            
        return max(maxSubstring, r - l)
            
            