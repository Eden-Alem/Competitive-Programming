class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c:c[1])
        
        heap = []
        time = 0
        for d, l in courses:
            heapq.heappush(heap, -d)
            time += d
            
            if time > l:
                time -= -(heapq.heappop(heap))
                
        
        return len(heap)