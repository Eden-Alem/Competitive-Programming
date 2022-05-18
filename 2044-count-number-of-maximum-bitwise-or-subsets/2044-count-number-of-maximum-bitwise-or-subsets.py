class Solution:
    def __init__(self):
        self.count = 0
        
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = nums[0]
        n = len(nums)
        
        for i in range(1, n):
            maxOr = maxOr | nums[i]
        
        result = []
        for n in range(2**len(nums)):
            curr = 0
            for j in range(len(nums)):
                if (n & (1 << j)) > 0:                    
                    curr = curr | nums[j]
              
            if curr == maxOr:
                self.count += 1
                
        return self.count