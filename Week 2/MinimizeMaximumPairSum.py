class Solution:
    def minPairSum(self, nums):
        nums.sort()
        result = []
        i = 0
        j = len(nums)-1
        
        while (i <= j):
            result.append([nums[i], nums[j]])
            i += 1
            j -= 1
        
        return max(x[0]+x[1] for x in result)