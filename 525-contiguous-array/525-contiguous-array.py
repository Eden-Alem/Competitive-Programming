class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        counts[0] = -1
        count = 0
        maxLen = 0
        for i, n in enumerate(nums):
            count += 1 if n == 1 else -1
            
            if count in counts:
                maxLen = max(maxLen, i - counts[count])
            else:
                counts[count] = i
                
        return maxLen
                
            
        
        