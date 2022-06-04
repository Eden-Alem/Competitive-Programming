class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result, columns, leftDiag, rightDiag = [], set(), set(), set()
		
        def backtrack(r, pos): 
            if r == n:
                result.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in pos])
                return
            for c in range(n):
                if not c in columns and not r - c in leftDiag and not r + c in rightDiag:
                    columns.add(c)
                    leftDiag.add(r - c)
                    rightDiag.add(r + c)
                    backtrack(r + 1, pos + [c])
                    columns.remove(c)
                    leftDiag.remove(r - c)
                    rightDiag.remove(r + c)
            
        backtrack(0, [])
        return result
        