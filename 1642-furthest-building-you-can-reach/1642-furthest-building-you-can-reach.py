class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        difference = [0]
        
        for h in range(len(heights)-1):
            if heights[h+1] > heights[h]:
                difference.append(heights[h+1] - heights[h])
            else:
                difference.append(0)
        
        
        for diff in range(len(difference)):
            
            if difference[diff] == 0:
                continue
                
            heapq.heappush(heap, difference[diff])
            
            if (len(heap) > ladders):                    
                bricks -= heapq.heappop(heap)
                
            if (bricks < 0):
                return diff - 1

        return len(heights) - 1
        
            
        
        
        
        
        
                            
                            