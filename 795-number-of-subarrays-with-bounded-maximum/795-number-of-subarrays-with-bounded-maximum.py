class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:                
        l, r = -1, -1
        max_count = 0
        
        for i in range(len(nums)):
            if nums[i] > right:
                l = r = i
                continue
                
            if nums[i] >= left:
                r = i
                
            max_count += (r - l)
               
        return max_count
    
    
        