class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        unique = set()
        
        result = 0
        while (r < len(s)):
            while (s[r] in unique):
                unique.remove(s[l])
                l += 1
                
            unique.add(s[r])
            result = max(result, r - l + 1)
            
            r += 1
            
        return result