class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        
        result = 0
        for i in range(len(boxTypes)):
            box = boxTypes[i][0]
            unit = boxTypes[i][1]
            
            if truckSize >= box:
                truckSize -= box
                result += (unit * box)
                
            else:
                result += (unit * truckSize)
                break
                
        return result
        