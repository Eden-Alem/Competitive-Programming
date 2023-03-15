class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        response = []
        for word in words:
            if self.isVowel(word):
                response.append(1)
            else:
                response.append(0)
                
        prefix = [0]
        for i in range(len(response)):
            prefix.append((prefix[-1] + response[i]))
          
        result = []
        for query in queries:
            l, r = query[0], query[1]
            
            result.append((prefix[r+1] - prefix[l]))
            
        return result
        
        
    def isVowel(self, word):
        vowels = set(['a','e','i','o','u'])
        
        return (word[0] in vowels) and (word[-1] in vowels)
        