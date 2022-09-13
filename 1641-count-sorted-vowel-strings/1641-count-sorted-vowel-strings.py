class Solution:
    def countVowelStrings(self, n: int) -> int:
        matrix = [[0] * 5 for _ in range(n)]
        
        matrix[0] = [1] * 5
        
        
        for i in range(1, len(matrix)):
            matrix[i][4] = matrix[i-1][4]
            matrix[i][3] = matrix[i-1][3] + matrix[i][4]
            matrix[i][2] = matrix[i-1][2] + matrix[i][3]
            matrix[i][1] = matrix[i-1][1] + matrix[i][2]
            matrix[i][0] = matrix[i-1][0] + matrix[i][1]
            
            
        return sum(matrix[-1])
            