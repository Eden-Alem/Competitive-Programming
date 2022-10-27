class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        count = 0
        for n in nums:            
            if (n-1) not in numSet:
                tempCount = 1
                while (n + tempCount) in numSet:
                    tempCount += 1
                    
                count = max(count, tempCount)
            
        return count