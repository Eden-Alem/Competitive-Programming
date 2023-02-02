class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = defaultdict(list)
        for i, n in enumerate(nums):
            count[n].append(i)
            
        result = 0
        for num in count:
            for i in range(len(count[num])):
                result += i
                
        return result
    
        