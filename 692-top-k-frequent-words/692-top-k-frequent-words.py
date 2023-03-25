class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        
        heap = []
        for key, val in frequency.items():
            heapq.heappush(heap, (-val, key))
            
        result = []
        while k:
            result.append(heapq.heappop(heap)[1])
            k -= 1
            
        return result
        