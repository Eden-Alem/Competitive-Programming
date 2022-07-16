class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numsSet = set()
        N = len(nums)
        for n in nums:
            if n >= 1:
                numsSet.add(n)
                
        for num in range(1, N+2):
            if num not in numsSet:
                return num
            
            
        