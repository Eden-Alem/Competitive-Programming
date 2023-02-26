class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                
        result = 0
        while zeros != n:
            m = self.findMin(nums)
            for i in range(n):
                if nums[i]:
                    nums[i] -= max(m, 0)
                    if nums[i] == 0:
                        zeros += 1
            result += 1
            
        return result
        
    def findMin(self, nums):
        minimum = float("inf")
        for i in range(len(nums)):
            if nums[i] < minimum and nums[i] != 0:
                minimum = nums[i]
                
        return minimum
        