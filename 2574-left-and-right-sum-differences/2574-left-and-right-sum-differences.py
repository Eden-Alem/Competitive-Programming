class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]
        
        for i in range(n-1):
            prefix.append((prefix[-1] + nums[i]))
        
        postfix = [0]
        for i in range(n-1,0,-1):
            postfix.append((postfix[-1] + nums[i]))
            
        postfix.reverse()
        
        result = []
        for i in range(n):
            result.append(abs(prefix[i] - postfix[i]))
            
        return result
        