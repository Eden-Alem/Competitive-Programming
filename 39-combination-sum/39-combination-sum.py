class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        result = []
        
        def combination(i, comb, total):
            if total == target:
                result.append(comb.copy())
                return
            
            if total > target or i >= n:
                return
            
            comb.append(candidates[i])
            combination(i, comb, total + candidates[i])
            comb.pop()
            combination(i+1, comb, total)
           
        combination(0, [], 0)
        return result