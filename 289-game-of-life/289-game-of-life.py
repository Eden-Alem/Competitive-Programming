class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        0 0 0
        1 0 1
        0 1 2
        1 1 3
        """
        n, m = len(board), len(board[0])
        direction = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
        
        in_bound = lambda new_row, new_col: new_row < 0 or new_col < 0 or new_row >= n or new_col >= m
        
        def numOfNeighbours(r, c):
            num = 0
            for row, col in direction:
                new_row = row + r
                new_col = col + c
                
                if in_bound(new_row, new_col):
                    continue
                    
                if board[new_row][new_col] in [1, 3]:
                    num += 1
                    
            return num
        
        for r in range(n):
            for c in range(m):
                neighbours = numOfNeighbours(r, c)
                
                if board[r][c]:
                    if neighbours in [2, 3]:
                        board[r][c] = 3
                        
                else:
                    if neighbours == 3:
                        board[r][c] = 2
                        
        for r in range(n):
            for c in range(m):
                if board[r][c] in [2, 3]:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
                    
            
                        
                    
            
        