class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        if not s:
            return 0
        
        i = 0
        n = len(s)
        sign = 1
        
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
          
        num = 0
        while i < n:
            char = s[i]
            
            if not char.isdigit():
                break
                
            else:
                num = (num * 10) + int(char)
                
            i += 1
                
        num *= sign
        
        if num > 2**31 - 1:
            return 2**31 - 1
        elif num < -2**31:
            return -2**31
        
        return num
        