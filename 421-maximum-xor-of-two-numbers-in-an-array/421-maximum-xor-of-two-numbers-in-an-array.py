class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxResult = 0
        n = len(bin(max(nums))) - 2
        
        for i in range(n,-1,-1):
            maxResult <<= 1
            currentMax = maxResult | 1
            
            currentSet = set()
            for num in nums:
                currentSet.add(num >> i)
                
            for val in currentSet:
                if (val ^ currentMax) in currentSet:
                    maxResult = currentMax
                    break
                    
        return maxResult
        