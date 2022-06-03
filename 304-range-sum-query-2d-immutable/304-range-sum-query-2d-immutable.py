class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, columns = len(matrix), len(matrix[0])
        self.prefixMatrix = [[0] * (columns+1) for _ in range(rows+1)]
        
        for r in range(rows):
            prefix = 0
            for c in range(columns):
                prefix += matrix[r][c]
                
                self.prefixMatrix[r+1][c+1] = prefix + self.prefixMatrix[r][c+1]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomR = self.prefixMatrix[row2+1][col2+1]
        upper = self.prefixMatrix[row1][col2+1]
        left = self.prefixMatrix[row2+1][col1]
        topL = self.prefixMatrix[row1][col1]
        
        return bottomR - upper - left + topL
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)