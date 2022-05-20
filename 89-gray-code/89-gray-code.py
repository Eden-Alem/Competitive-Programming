class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        self.checkSequence(n, result, 0, set([0]))
        return result
        
    def checkSequence(self, n, result, curr, visited):
        if len(result) == 2**n:
            return True
        
        
        for i in range(n):            
            val = curr ^ (1 << i)
            
            if val not in visited:
                visited.add(val)
                result.append(val)
                
                if self.checkSequence(n, result, val, visited):
                    return True
                
                visited.remove(val)
                result.pop()
                
        return False
        
                