class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder = defaultdict(int)
        remainder[0] += 1
        
        sum_, count = 0, 0
        
        for num in nums:
            sum_ += num
            
            if (sum_ % k in remainder):
                count += remainder[(sum_ % k)]
        
            remainder[(sum_ % k)] += 1
            
            
        return count