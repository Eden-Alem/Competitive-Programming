class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        unique = set()
        running_sum = 0
        erasureVal = 0
        
        for right in range(n):
            while nums[right] in unique and left <= right:
                unique.remove(nums[left])                
                running_sum -= nums[left]
                left += 1
            
            unique.add(nums[right])
            running_sum += nums[right]
            erasureVal = max(erasureVal, running_sum)
            
        return erasureVal