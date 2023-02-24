class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N = len(nums)
        result = 0
        
        for i in range(N):
            minVal = nums[i]
            maxVal = nums[i]
            
            for j in range(i+1, N):
                minVal = min(minVal, nums[j])
                maxVal = max(maxVal, nums[j])
                
                result += (maxVal - minVal)
                
        return result
                
            