class Solution:
    def smallerNumbersThanCurrent(self, nums):
        smaller = [0] * len(nums)
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if ((i != j) and (nums[j] < nums[i])):
                    smaller[i] += 1
        
        return smaller