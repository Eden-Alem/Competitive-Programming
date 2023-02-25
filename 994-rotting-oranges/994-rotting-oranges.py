class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        left_over = 0
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r,c])
                    
                if grid[r][c] == 1:
                    left_over += 1
        
        time = 0
        directional = [[0,1],[0,-1],[-1,0],[1,0]]
        while queue and left_over:
            for i in range(len(queue)):
                orange = queue.popleft()
                
                for direction in directional:
                    new_row = direction[0] + orange[0]
                    new_col = direction[1] + orange[1]
                    
                    if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS:
                        continue
                        
                    if grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append([new_row, new_col])
                        left_over -= 1
                        
            time += 1
            
        return -1 if left_over else time
                    
        