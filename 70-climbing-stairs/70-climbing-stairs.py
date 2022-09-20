class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        
        def climbing(k):
            if k > n: return 0
            
            if k == n: return 1
            
            if k in mem:
                return mem[k]
            
            one = two = 0
            one += climbing(k+1)
            two += climbing(k+2)
            
            mem[k] = one + two
            return one + two
        
        return (climbing(0))