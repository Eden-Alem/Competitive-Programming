class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])
            
        left = 1
        while (left < len(prefix)):
            if (prefix[left - 1] == prefix[-1] - prefix[left]):
                return left - 1
            left += 1
            
        return -1