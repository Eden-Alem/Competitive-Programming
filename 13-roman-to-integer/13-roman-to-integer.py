class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        n = len(s)
        result = 0
        
        for i in range(n):
            if i+1 < n and symbols[s[i]] < symbols[s[i+1]]:
                result -= symbols[s[i]]
                
            else:
                result += symbols[s[i]]
                
        return result
        