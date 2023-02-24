class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        
        freq = Counter(s)
        
        for char, count in freq.items():
            heapq.heappush(maxHeap, (-count, char))
            
        result = ""
        prev = None
        
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            
            count, char = heapq.heappop(maxHeap)
            result += char
            count += 1  
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if count != 0:
                prev = (count, char)
            
            
        return result
                
            