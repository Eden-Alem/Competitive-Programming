class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        commonString = self.commonSequence(word1, word2, 0, 0, {})
        return (len(word1) - commonString) + (len(word2) - commonString)
        
    def commonSequence(self, word1, word2, index1, index2, memo):
        if index1 == len(word1) or index2 == len(word2):
            return 0
        
        if (index1, index2) in memo:
            return memo[(index1, index2)]
        
        if word1[index1] == word2[index2]:
            memo[(index1, index2)] = 1 + self.commonSequence(word1, word2, index1+1, index2+1, memo)
        else:
            memo[(index1, index2)] = max(self.commonSequence(word1, word2, index1+1, index2, memo), self.commonSequence(word1, word2, index1, index2+1, memo))
            
        return memo[(index1, index2)]