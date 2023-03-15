class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append((prefix[-1] + num))
            
        postfix = [0]
        for num in reversed(nums):
            postfix.append((postfix[-1] + num))
            
        postfix.reverse()
        
        for i in range(1, len(prefix)):
            if prefix[i-1] == postfix[i]:
                return i-1
            
        return -1