class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: int(x[0]))
        
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):             
            if (result[-1][1] >= intervals[i][0]):                    
                result[-1] = [min(result[-1][0], intervals[i][0]), max(result[-1][1], intervals[i][1])]
            else:                        
                result.append(intervals[i])               
        
        return result
        