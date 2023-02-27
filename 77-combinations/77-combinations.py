class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(i, comb):
            if len(comb) == k:
                result.append(comb.copy())
                return
            
            for j in range(i, n+1):
                comb.append(j)
                backtrack(j+1, comb)
                comb.pop()
                
        backtrack(1, [])
        return result
        