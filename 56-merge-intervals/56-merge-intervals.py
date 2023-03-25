class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        result = [intervals[0]]
        
        for s, e in intervals[1:]:
            prev_e = result[-1][1]
            
            if s <= prev_e:
                result[-1][1] = max(prev_e, e)
                
            else:
                result.append([s, e])
                
        return result