class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)%2 != 0):
            return False
        
        stack = []
        
        parens = {"(": ")", "[": "]", "{": "}"}
        
        for paren in s:
            if paren in parens.keys():
                stack.append(paren)
            elif paren in parens.values():
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if parens[p] != paren:
                    return False
                
        return True if len(stack) == 0 else False
                
            