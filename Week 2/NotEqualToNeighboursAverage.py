class Solution:
    def rearrangeArray(self, nums):
        nums.sort()
        result = []
        
        left, right = 0, len(nums) - 1
        while len(result) != len(nums):
            result.append(nums[left])
            left += 1
            
            if(left <= right):
                result.append(nums[right])
                right -= 1
                
        return result