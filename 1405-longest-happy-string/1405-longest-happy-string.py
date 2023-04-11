class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        
        if c: heapq.heappush(maxHeap, (-c, "c"))
            
        if b: heapq.heappush(maxHeap, (-b, "b"))
            
        if a: heapq.heappush(maxHeap, (-a, "a"))
        
        result = ""
        while maxHeap:
            
            count, char = heapq.heappop(maxHeap)
            
            if len(result) >= 2 and result[-2:] in ["cc", "aa", "bb"]:
                
                if char == result[-1]:
                    if maxHeap:
                        new_count, new_char = heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap, (count, char))
                        result += new_char
                        new_count += 1
                        if new_count:
                            heapq.heappush(maxHeap, (new_count, new_char))
                    continue
            
            result += char
            count += 1
            if count:
                heapq.heappush(maxHeap, (count, char))
                
        return result
                
                
            
        