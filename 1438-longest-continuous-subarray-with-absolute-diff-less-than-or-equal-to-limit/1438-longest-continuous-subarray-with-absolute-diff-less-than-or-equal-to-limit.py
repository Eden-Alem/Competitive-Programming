class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        right = 0
        
        incDeq = Deque()
        decDeq = Deque()
        
        result = 0
        while (right < len(nums)):
            while (len(incDeq) and nums[right] <= nums[incDeq[-1]]):
                incDeq.pop()
            incDeq.append(right)
                
            while (len(decDeq) and nums[right] >= nums[decDeq[-1]]):
                decDeq.pop()
            decDeq.append(right)
            
            if (abs(nums[decDeq[0]] - nums[incDeq[0]]) > limit):
                left += 1
                if (left > decDeq[0]): decDeq.popleft()
                if (left > incDeq[0]): incDeq.popleft()
            else:
                result = max(result, right-left+1)
                right += 1
            
        return result