class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        last_end = intervals[0][1]
        to_remove = 0
        
        for start, end in intervals[1:]:
            
            if start < last_end:
                last_end = min(last_end, end)
                to_remove += 1
                
            else:
                last_end = end
                
        return to_remove
        