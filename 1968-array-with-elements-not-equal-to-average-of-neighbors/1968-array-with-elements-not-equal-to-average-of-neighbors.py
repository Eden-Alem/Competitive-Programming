class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        left, right = 0, len(nums)-1
        
        result = []
        while len(result) != len(nums):
            result.append(nums[left])
            left += 1
            
            if left <= right:
                result.append(nums[right])
                right -= 1
                
        return result
        