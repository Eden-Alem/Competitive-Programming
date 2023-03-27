class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        prefix = []
        suffix = []
        
        cur_max = float("-inf")
        for a in arr:
            cur_max = max(a, cur_max + a)
            prefix.append(cur_max)
            
        cur_max = float("-inf")
        for a in reversed(arr):
            cur_max = max(a, cur_max + a)
            suffix.append(cur_max)
            
        suffix.reverse()
        
        max_sum = float("-inf")
        n = len(arr)
        
        for i in range(n):
            if i == 0:
                sum_ = suffix[i]
                
            elif i == n-1:
                sum_ = prefix[i]
                
            else:
                sum_ = max(prefix[i-1] + suffix[i+1], suffix[i], prefix[i])
                
            max_sum = max(max_sum, sum_)
            
        return max_sum
            
        
        
        