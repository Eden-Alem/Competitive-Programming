class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        
        for n in nums:
            xor ^= n
            
        xor &= -xor
        
        result = [0, 0]
        for n in nums:
            if (xor & n == 0):
                result[0] ^= n
                
            else:
                result[1] ^= n
                
        return result