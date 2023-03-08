class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        temp = self.getRow(rowIndex - 1)
        temp = [0] + temp + [0]
        result = []
        
        for i in range(1, len(temp)):
            result.append(temp[i-1] + temp[i])
            
        return result
        