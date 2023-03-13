class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixNums = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefixNums[i+1] =  prefixNums[i] + nums[i]
        
        result = 0
        pre = {}
        for n in prefixNums:                       
            result += pre.get(n - k, 0)
            pre[n] = 1 + pre.get(n, 0) 
            
        return result