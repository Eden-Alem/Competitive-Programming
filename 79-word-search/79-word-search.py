class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= n or c >= m or word[i] != board[r][c] or (r,c) in path:
                return False
            
            path.add((r,c))
            result = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            path.remove((r,c))
            
            return result
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                    
        return False 
                    
            
        