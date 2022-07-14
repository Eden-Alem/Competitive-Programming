class Solution:
    def __init__(self):
        self.directional = [[0,1],[1,0],[-1,0],[0,-1]]
        self.visited = set()
        
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [["0" for _ in range(n)] for _ in range(m)]
        
        for i,j in walls:
            matrix[i][j] = "W"
        
        for i, j in guards:
            matrix[i][j] = "G"
            
        directional = [[0,1],[1,0],[0,-1],[-1,0]]
            
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "G":
                    self.iterateInDirection(r,c+1,matrix,directional[0])
                    self.iterateInDirection(r+1,c,matrix,directional[1])
                    self.iterateInDirection(r,c-1,matrix,directional[2])
                    self.iterateInDirection(r-1,c,matrix,directional[3])
                    
        count = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "0":
                    count += 1
        
        return count
        
    def iterateInDirection(self, r, c, matrix, direction):        
        if (r < 0 or c < 0 or r > len(matrix)-1 or c > len(matrix[0])-1):
                return   
            
        if (matrix[r][c] == "G" or matrix[r][c] == "W"):
            return      
        
        matrix[r][c] = "1"
        
        row = r + direction[0]
        column = c + direction[1]
        self.iterateInDirection(row, column, matrix, direction)  
                
                
            

        