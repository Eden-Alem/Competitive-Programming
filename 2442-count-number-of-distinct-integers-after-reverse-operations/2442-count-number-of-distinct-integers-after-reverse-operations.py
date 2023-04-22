class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = set(nums)
        
        for num in nums:
            s = str(num)[::-1]
            
            result.add(int(s))
            
        return len(result)
        