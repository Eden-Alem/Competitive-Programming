class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        n = len(timePoints)
        for time in range(n):
            temp = timePoints[time].split(":")
            hour = int(temp[0])
            minute = int(temp[1])
            minutes.append((hour*60)+minute)
            
        minutes.sort()
        
        minDifference = minutes[0] - minutes[-1] + 1440
        N = len(minutes)
        for minute in range(1, N):
            minDifference = min(minDifference, minutes[minute] - minutes[minute-1])
            
        return minDifference
            
            
            