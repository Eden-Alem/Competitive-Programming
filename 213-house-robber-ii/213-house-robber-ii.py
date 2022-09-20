class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robbery(nums):
            rob1, rob2 = 0, 0
            n = len(nums)

            for i in range(n):
                temp = max(nums[i] + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
        
        return max(nums[0], robbery(nums[1:]), robbery(nums[:-1]))