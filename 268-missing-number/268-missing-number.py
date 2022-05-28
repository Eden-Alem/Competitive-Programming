class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            result ^= nums[i]
            result ^= i+1
            
        return result
        