class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixSums = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            prefixSums[i+1] = prefixSums[i] + nums[i]
        
        result = float('inf')
        monoQueue = Deque()
        for i in range(len(prefixSums)):
            while (len(monoQueue) and prefixSums[i] <= prefixSums[monoQueue[-1]]):
                monoQueue.pop()
            monoQueue.append(i)
            
            while (len(monoQueue) and prefixSums[i] - prefixSums[monoQueue[0]] >= k):
                result = min(result, i - monoQueue.popleft())
         
        return -1 if (result == float('inf')) else result