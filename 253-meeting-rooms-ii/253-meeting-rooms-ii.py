class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        
        for s, e in intervals:
            start.append(s)
            end.append(e)
            
        start.sort()
        end.sort()
        
        s, e = 0, 0
        n = len(intervals)
        rooms, count = 0, 0
        while s < n:
            if start[s] < end[e]:
                s += 1
                count += 1                
            else:
                e += 1
                count -= 1
                
            rooms = max(rooms, count)
                
        return rooms
        