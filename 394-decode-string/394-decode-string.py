class Solution:
    def decodeString(self, s: str) -> str:
        num = '0'
        alphabet = ''
        result = ''
        i = 0
        
        while (i < len(s)):
            if (s[i].isdigit()):
                num += s[i]
            elif (s[i] == '['):
                i += 1
                opening = 1
                while (opening != 0):
                    if (s[i] == '['):
                        opening += 1
                    if (s[i] == ']'):
                        opening -= 1
                    if (opening != 0):
                        alphabet += s[i]
                        i += 1
                alphabet = self.decodeString(alphabet)
                result += int(num) * alphabet
                
                num = '0'
                alphabet = ''  
                
            else:
                result += s[i]
            i += 1  
            
        return result