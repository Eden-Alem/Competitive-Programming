class Solution:
    def __init__(self):
        self.stack = []
        self.result = []
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.generate(n, 0, 0)
        return self.result
        
    def generate(self, n, on, cn):
        if (n == on == cn):
            return self.result.append("".join(self.stack))
        
        if on < n:
            self.stack.append("(")
            self.generate(n, on+1, cn)
            self.stack.pop()
            
        if cn < on:
            self.stack.append(")")
            self.generate(n, on, cn+1)
            self.stack.pop()
            
        
            