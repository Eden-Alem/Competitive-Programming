class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x:len(x))
        n = len(words)
        memo = {}
        
        for i in range(n):
            word = words[i]
            currentMax = 1
            for j in range(len(word)):
                temp = word[:j] + word[j+1:]
                if temp in memo:
                    currentMax = max(currentMax, memo[temp]+1)
                    
            memo[word] = currentMax
            
        return max(memo.values())
        