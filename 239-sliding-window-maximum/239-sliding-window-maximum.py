class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        
        for n in nums[:k]:
            while queue and queue[-1] < n:
                queue.pop()

            queue.append(n)
            
            
        def monotonic(n):
            while queue and queue[-1] < n:
                queue.pop()
                
            queue.append(n)

            
        n = len(nums)
        max_result = [queue[0]]
        for i in range(k, n):
            if nums[i - k] == queue[0]:
                queue.popleft()
                
            monotonic(nums[i])
            max_result.append(queue[0])
            
        return max_result
            
            
        