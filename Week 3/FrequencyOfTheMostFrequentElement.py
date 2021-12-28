class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        left = 0
        right = 0
        result = 1
        nums.sort()
        
        while(right < len(nums)-1):
            if (k >= 0):
                right += 1
                k -= (right - left) * abs(nums[right] - nums[right-1])
            else:
                k += abs(nums[right] - nums[left])
                left += 1
            
            if (k >= 0):
                result = max(result, right - left + 1)
        
        return result