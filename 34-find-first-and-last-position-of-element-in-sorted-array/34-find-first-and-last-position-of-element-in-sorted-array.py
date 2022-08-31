class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        starting, ending = -1, -1
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                starting = mid
                right = mid - 1
                
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                ending = mid
                left = mid + 1
                
        return [starting, ending]