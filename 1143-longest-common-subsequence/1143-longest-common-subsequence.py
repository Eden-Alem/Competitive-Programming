class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.commonSubsequence(text1, text2, 0, 0, {})
        
    def commonSubsequence(self, text1, text2, index1, index2, memo):
        if (index1 == len(text1) or index2 == len(text2)):
            return 0
        
        if (index1, index2) in memo:
            return memo[(index1, index2)]
        
        if text1[index1] == text2[index2]:
            memo[(index1, index2)] = 1 + self.commonSubsequence(text1, text2, index1+1, index2+1, memo)
        else:
            memo[(index1, index2)] = max(self.commonSubsequence(text1, text2, index1+1, index2, memo), self.commonSubsequence(text1, text2, index1, index2+1, memo))
            
        return memo[(index1, index2)]
            
        