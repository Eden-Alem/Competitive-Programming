class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        
        result = []
        for word in words:
            len_w = len(word)
            w = word[:len_w-1]
            n = int(word[len_w-1:])
            result.append((n, w))
        
        result.sort()
        output = []
        for w in result:
            output.append(w[1])
            
        return " ".join(output)
        