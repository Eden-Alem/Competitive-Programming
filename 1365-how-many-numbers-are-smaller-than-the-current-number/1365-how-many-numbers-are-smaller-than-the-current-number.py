class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        result = [0] * n
        
        for i in range(n):
            for j in range(n):
                if (j != i and nums[j] < nums[i]):
                    result[i] += 1
                    
        return result
                
        
        