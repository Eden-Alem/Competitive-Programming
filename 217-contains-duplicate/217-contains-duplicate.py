class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = {}
        
        for num in nums:
            if (num in frequency.keys()):
                return True
            else:
                frequency[num] = frequency.get(num, 0) + 1
            
        return False