class Solution:
    def partitionLabels(self, s: str):
        lastIndex = dict()
        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        result = []
        last = 0
        length = 0
        for i in range(len(s)):
            if last < lastIndex[s[i]]:
                last = lastIndex[s[i]]
                
            length += 1
            
            if i == last:
                result.append(length)
                length = 0
                
        return result