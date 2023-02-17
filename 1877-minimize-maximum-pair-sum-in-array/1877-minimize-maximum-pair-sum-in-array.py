class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        left, right = 0, n-1
        result = []
        
        while (left <= right):
            result.append((nums[left], nums[right]))
            left += 1
            right -= 1
            
        return max(i[0] + i[1] for i in result)
        