class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count_char = 0
        i, j = 0, 0
        
        while i < len(s):
            while j < len(t) and i < len(s) and t[j] == s[i]:
                count_char += 1
                j += 1
                i += 1
                
            i += 1
            
        return len(t) - count_char
        