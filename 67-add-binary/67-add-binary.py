class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        
        a = a.zfill(n)[::-1]
        b = b.zfill(n)[::-1]
        
        result = ""
        carry = 0
        
        for i in range(n):
            total = int(a[i]) + int(b[i]) + carry
            
            result += str(total % 2)
            
            carry = total // 2
            
            
        if carry: result += str(carry)
            
        return result[::-1]
        