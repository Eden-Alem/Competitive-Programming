class Solution:
    def findScore(self, nums: List[int]) -> int:
        minHeap = []
        
        for i, num in enumerate(nums):
            heapq.heappush(minHeap, (num, i))
            
        result = 0
        visited = set()
        
        for i in range(len(nums)):
            score, idx = heapq.heappop(minHeap)
            
            if idx not in visited:
                result += score
                
                visited.add(idx)
                visited.add(idx-1)
                visited.add(idx+1)
            
        return result
            
        