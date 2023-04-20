class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bann = set(banned)
        
        count = 0
        cur_sum = 0
        for num in range(1, n+1):
            if num not in bann:
                if cur_sum + num <= maxSum:
                    count += 1
                    cur_sum += num
                    
        return count