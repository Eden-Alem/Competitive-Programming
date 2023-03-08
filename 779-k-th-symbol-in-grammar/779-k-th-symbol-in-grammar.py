class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        parent = self.kthGrammar(n-1, ceil(k/2))
        isEven = (k%2 == 0)
        
        if parent == 1:
            return 0 if isEven else 1
        else:
            return 1 if isEven else 0
        
        