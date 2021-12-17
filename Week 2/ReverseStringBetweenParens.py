class Solution:
    def reverseParentheses(self, s: str) -> str:
        listS = []
        listS[:0] = s
        # print(listS)
        stackS = []
        parenDict = {")":"("}
        for i in range(len(listS)):
            if (")" != listS[i]):
                stackS.append(listS[i])
            else:
                temp = stackS[reverseIndex(stackS, parenDict[listS[i]]):]
                del stackS[reverseIndex(stackS, parenDict[listS[i]]):]
                
                temp.reverse()
                temp.pop()                
                
                stackS.extend(temp)
                
                
        return "".join(stackS)
        
def reverseIndex(arr, element):
    lastIndex = -1
    for i in range(len(arr)):
        if (arr[i] == element):
            lastIndex = i
    return lastIndex