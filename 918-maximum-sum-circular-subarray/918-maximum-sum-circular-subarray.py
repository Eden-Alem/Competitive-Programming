class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = 0
        max_sum = float("-inf")
        
        cur_min = 0
        min_sum = float("inf")
        
        total_sum = 0
        
        for num in nums:
            total_sum += num
            
            cur_max += num
            cur_max = max(cur_max, num)
            
            max_sum = max(max_sum, cur_max)
            
            cur_min += num
            cur_min = min(cur_min, num)
            
            min_sum = min(min_sum, cur_min)
            
        if max_sum < 0 and max_sum != float("-inf"):
            return max_sum
        
        return max(total_sum - min_sum, max_sum)
        
            
            
            
        