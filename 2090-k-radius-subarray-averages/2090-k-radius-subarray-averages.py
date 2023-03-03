class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if 2*k >= n:
            return [-1] * n
        
        result = [-1] * k
        
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        prefix.append(0)
        
        for i in range(k, n-k):
            avg = (prefix[i+k+1] - prefix[i-k])//(2*k + 1)
            result.append(avg)
            
        result.extend([-1]*k)
        
        return result

        
        