class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
         # [-2,1,-3,4,-1,2,1,-5,4]
        
        a = 0
        b = float("-inf")
        for n in nums:
            a += n
            if a > b:
                b = a
            if a < 0:
                a = 0
        return b