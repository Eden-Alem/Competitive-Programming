class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0
        
        frequency = {}
        maxChar = 0
        longestSubstr = 0
        
        while r < n:
            frequency[s[r]] = frequency.get(s[r], 0) + 1
            maxChar = max(maxChar, frequency[s[r]])
            
            while ((r-l+1) - maxChar > k):
                frequency[s[l]] -= 1
                l += 1
              
            longestSubstr = max(longestSubstr, r - l + 1)
            r += 1
            
        return longestSubstr
            