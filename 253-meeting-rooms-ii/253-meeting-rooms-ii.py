class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = [intervals[0][1]]
        n = len(intervals)
        
        for i in range(1, n):
            start, end = intervals[i]
            
            if rooms[0] > start:
                heapq.heappush(rooms, end)
                
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms, end)
                
        return len(rooms)
        