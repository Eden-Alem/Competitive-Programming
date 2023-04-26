class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        w1 = [0] * 26
        w2 = [0] * 26
        
        for w in word1:
            w1[ord(w) - ord('a')] += 1
            
        for w in word2:
            w2[ord(w) - ord('a')] += 1
            
        for i in range(26):
            if w1[i] > 0:
                for j in range(26):
                    if w2[j] > 0:
                        self.swap(w1,w2,i,j)
                        
                        if self.isEqual(w1,w2):
                            return True
                        
                        self.swap(w1,w2,j,i)
                        
        return False
                
            
    def swap(self, w1, w2, i, j):
        w1[i] -= 1
        w2[i] += 1
        w2[j] -= 1
        w1[j] += 1 
        
    def isEqual(self, w1, w2):
        count = 0
        for i in range(26):
            if w1[i] > 0:
                count += 1
            if w2[i] > 0:
                count -= 1
                
        return count == 0
        
