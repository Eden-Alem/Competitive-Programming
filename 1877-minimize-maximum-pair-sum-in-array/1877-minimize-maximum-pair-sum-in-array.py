class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        l, r = 0, n-1
        result = []
        
        while (l <= r):
            result.append((nums[l], nums[r]))
            l += 1
            r -= 1
            
        return max(i[0] + i[1] for i in result)
        