class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        
        if n < 5:
            return 0
        
        max_len = 0
        cur_len = 1
        
        distinct = 1
        
        for i in range(1, n):
            if word[i-1] <= word[i]:
                if word[i-1] != word[i]:
                    distinct += 1
                    
                cur_len += 1
            else:
                if distinct == 5:
                    max_len = max(max_len, cur_len)
                    
                distinct = 1
                cur_len = 1
                
        if distinct == 5:
            max_len = max(max_len, cur_len)
            
        return max_len
                
                
        