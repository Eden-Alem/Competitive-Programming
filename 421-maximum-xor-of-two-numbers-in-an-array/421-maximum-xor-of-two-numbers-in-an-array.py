class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxRes = 0
        l = len(bin(max(nums)))-2
        for i in range(l,-1,-1):            
            currMax = maxRes | 1
            
            currSet = set()
            for n in nums:
                currSet.add(n >> i)            
            
            for k in currSet:
                if (k ^ currMax) in currSet:
                    maxRes = currMax 
                    break
                    
            if i != 0:        
                maxRes <<= 1
                
        return maxRes
        