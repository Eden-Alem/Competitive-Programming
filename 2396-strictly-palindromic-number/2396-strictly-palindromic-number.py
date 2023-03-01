class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n-1):
            arr = self.numberToBase(n, base)
            if not self.isPalindromic(arr):
                return False
            
        return True
            
        
        
    def numberToBase(self, n, b):
        if n == 0:
            return [0]
        
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
            
        return digits[::-1]
    
    def isPalindromic(self, arr):
        n = len(arr)
        l, r = 0, n-1
        
        while l < r:
            if arr[l] == arr[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True
        