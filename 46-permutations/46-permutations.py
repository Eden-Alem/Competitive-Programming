class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        if n == 1:
            return [nums.copy()]
        
        result = []
        
        for i in range(n):
            num = nums.pop(0)
            
            permutations = self.permute(nums)
            for perm in permutations:
                perm.append(num)
                
            result.extend(permutations)
            
            nums.append(num)
            
        return result
        