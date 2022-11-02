class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or token.lstrip('-').isdigit():
                stack.append(token)
            else:
                if (len(stack) >= 2):
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(str(int(eval(op1 + token + op2))))
                
                    
        return stack[-1]
                    