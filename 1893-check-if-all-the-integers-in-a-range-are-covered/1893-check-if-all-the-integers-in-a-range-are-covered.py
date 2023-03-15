class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        prefix = [0] * 52
        for s, e in ranges:
            prefix[s] += 1
            prefix[e+1] -= 1
            
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1] 
            
        for i in range(len(prefix)):
            if prefix[i] > 0:
                prefix[i] = 1
                
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1] 
            
        return prefix[right] - prefix[left-1] == (right - left + 1)