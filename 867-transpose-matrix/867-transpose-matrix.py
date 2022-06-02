class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposeMatrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j, val in enumerate(matrix[i]):
                transposeMatrix[j][i] = val
                
        return transposeMatrix