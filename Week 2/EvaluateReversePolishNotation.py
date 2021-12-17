class Solution:
    def evalRPN(self, tokens) -> int:
        numStack = []
        result = 0
        for i in range(len(tokens)):
            if (tokens[i].isdigit() or tokens[i].lstrip('-').isdigit()):
                numStack.append(tokens[i])
            else:
                if (len(numStack) >= 2):
                    secondNum = numStack.pop()
                    firstNum = numStack.pop()
                    result = int(eval(firstNum + tokens[i] + secondNum))
                    numStack.append(str(result))
                    
        return numStack.pop()