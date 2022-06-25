class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        used = False
        n = len(nums)
        
        for i in range(n-1):
            if nums[i] <= nums[i+1]:
                continue
                
            if used: return False
            
            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
                
            used = True
            
        return True