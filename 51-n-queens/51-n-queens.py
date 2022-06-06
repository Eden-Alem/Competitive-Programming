class Solution:
    def __init__(self):
        self.result = []
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posDiag, negDiag = set(), set(), set()
        
        chessBoard = [["."]*n for _ in range(n)]
        def backtrack(row):
            if row == n:
                self.result.append(["".join(r) for r in chessBoard])
                return
            
            for col in range(n):
                if col in cols or (row+col) in posDiag or (row-col) in negDiag:
                    continue
                    
                cols.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                chessBoard[row][col] = "Q"
                
                backtrack(row+1)
                
                cols.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)
                chessBoard[row][col] = "."
                
        backtrack(0)
        return self.result
        
        