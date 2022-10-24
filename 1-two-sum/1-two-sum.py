class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        pairMap = {}
        
        for i in range(n):
            temp = target - nums[i]
            if (temp in pairMap):
                return [pairMap[temp], i]
            
            pairMap[nums[i]] = i
            
        return