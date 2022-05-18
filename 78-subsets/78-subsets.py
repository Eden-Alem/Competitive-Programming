class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for n in range(2**len(nums)):
            temp = []
            for j in range(len(nums)):
                if (n & (1 << j)) > 0:                    
                    temp.append(nums[j])
                    
            result.append(temp)
            
        return result
        
    