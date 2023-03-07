class Solution:
    def decodeString(self, s: str) -> str:
        
        result = ''
        i = 0
        num = '0'
        chars = ''
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
                
            elif s[i] == '[':
                i+=1
                o = 1
                while o != 0:
                    if s[i] == '[':
                        o += 1
                    if s[i] == ']':
                        o -= 1
                    if o != 0:
                        chars += s[i]
                        i += 1
                chars = self.decodeString(chars)
                result += (int(num) * chars)
                
                num = '0'
                chars = ''
                
            else:
                result += s[i]
            
            i += 1
            
        return result
                
        