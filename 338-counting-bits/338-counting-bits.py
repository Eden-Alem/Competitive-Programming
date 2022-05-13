class Solution:
    def countBits(self, n: int) -> List[int]:        
        memo = [0] * (n+1)
        power = 1
        pointer = 1
        
        for i in range(1, n+1):
            if i == power:
                memo[i] = 1
                pointer = 1
                power <<= 1
            else:
                memo[i] = memo[pointer] + 1
                pointer += 1
                
        return memo
            
            
        