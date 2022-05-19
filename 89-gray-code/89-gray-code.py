class Solution:    
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        self.checker(n, set([0]), 0, result)
        return result
        
    def checker(self, n, visited, curr, result):
        if len(result) == 2**n:
            return True
        
        for i in range(n):            
            nextFlip = curr ^ (1 << i)
            
            if nextFlip not in visited:
                visited.add(nextFlip)
                result.append(nextFlip)
                if self.checker(n, visited, nextFlip, result):
                    return True
                
                visited.remove(nextFlip)
                result.pop()
                
        return False
        
        