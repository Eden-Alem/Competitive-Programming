class Solution:
    def __init__(self):
        self.result = 0
        
    def totalNQueens(self, n: int) -> int:
        columns, leftDiag, rightDiag = set(), set(), set()
		
        def backtrack(r): 
            if r == n:
                self.result += 1
                return
            for c in range(n):
                if c in columns or (r - c) in leftDiag or (r + c) in rightDiag:
                    continue
                columns.add(c)
                leftDiag.add(r - c)
                rightDiag.add(r + c)
                backtrack(r + 1)
                columns.remove(c)
                leftDiag.remove(r - c)
                rightDiag.remove(r + c)
            
        backtrack(0)
        return self.result