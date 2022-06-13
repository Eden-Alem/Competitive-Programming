class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        paths = [0] * (len(triangle[-1])+1)
        
        for i in range(len(triangle)-1,-1,-1):
            for j in range(len(triangle[i])):                
                paths[j] = min(triangle[i][j] + paths[j], triangle[i][j] + paths[j+1])
        
        return paths[0]

        