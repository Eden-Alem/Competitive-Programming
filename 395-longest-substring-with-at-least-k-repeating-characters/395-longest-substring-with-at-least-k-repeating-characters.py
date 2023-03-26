class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def substring(s, l, r):
            if r - l < k:
                return 0
            
            frequency = Counter(s[l:r])
            
            for i in range(l, r):
                if frequency[s[i]] < k:
                    j = i+1
                    
                    while j < r and frequency[s[j]] < k:
                        j += 1
                        
                    return max(substring(s, l, i), substring(s, j, r))
                
            return r - l
        
        return substring(s, 0, len(s))
            
                
        