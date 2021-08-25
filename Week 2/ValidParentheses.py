class Solution(object):
    def isValid(self, parentheses):
        openParentheses = ['[','{','(']
        closeParentheses = [']','}',')']
        checker = []
        for i in range(len(parentheses)):
            if parentheses[i] in openParentheses:
                checker.append(parentheses[i])
            else:
                if (len(checker) == 0):
                    return False
                if (closeParentheses.index(parentheses[i]) == openParentheses.index(checker[-1])):
                    checker.pop()
                else:
                    return False
        if (len(checker) == 0):
            return True
        else:
            return False
            
print(Solution().isValid("[{)}]()"))