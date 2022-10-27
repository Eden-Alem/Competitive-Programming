class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        pre = 1
        
        for i in range(n):
            result.append(pre)
            pre *= nums[i]
            
        post = 1
        for j in range(n-1,-1,-1):
            result[j] *= post
            post *= nums[j]
            
        return result
            