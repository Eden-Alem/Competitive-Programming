class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        
        for i in range(n):
            min_val = nums[i]
            max_val = nums[i]
            
            for j in range(i+1, n):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                
                result += (max_val - min_val)
                
        return result
        