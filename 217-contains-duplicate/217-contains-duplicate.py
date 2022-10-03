class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        
        for n in nums:
            freq[n] = (freq.get(n, 0) + 1)
            
        for val in list(freq.values()):
            if val >= 2:
                return True
            
        
        return False