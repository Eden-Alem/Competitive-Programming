class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        
        for i in range(n-3,-1,-1):
            nums[i] = max(nums[i]+nums[i+2], nums[i+1])
            
        return nums[0]