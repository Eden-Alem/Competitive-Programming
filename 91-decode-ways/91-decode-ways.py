class Solution:
    def __init__(self):
        self.mem = {}
        
    def numDecodings(self, s: str) -> int:
        self.mem[len(s)] = 1
        
        return self.decoding(0, s)
        
    def decoding(self, i, s):
        if i in self.mem:
            return self.mem[i]
        
        if s[i] == "0":
            return 0
        
        result = self.decoding(i+1, s)
        if (i + 1 < len(s)) and ((s[i] == "1") or (s[i] == "2" and s[i+1] in "0123456")):
            result += self.decoding(i+2, s)
            
        self.mem[i] = result
        
        return result
            