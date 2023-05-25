class Solution:
    def minOperations(self, n: int) -> int:
        if n > 0 and n == pow(2, int(math.log(n, 2))):
            return 1
        
        left, right = pow(2, int(math.log(n, 2))), pow(2, int(math.log(n, 2))+1)
        
        diff_left, diff_right = n - left, right - n
        
        return 1 + min(self.minOperations(diff_left), self.minOperations(diff_right))
        