class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        n = len(grid)
        m = len(grid[0])
        visited = set()
        
        in_bound = lambda new_row, new_col: new_row < 0 or new_row >= n or new_col < 0 or new_col >= m
        
        def dfs(row, col):
            visited.add((row, col))
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                
                if in_bound(new_row, new_col):
                    continue
                    
                if (new_row, new_col) not in visited and grid[new_row][new_col] == "1":
                    grid[new_row][new_col] = "2"
                    visited.add((new_row, new_col))
                    
                    dfs(new_row, new_col)
        
        result = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    dfs(r, c)
                    result += 1
            
        return result