class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        alphabets = {}
        
        for a in "qwertyuiop":
            alphabets[a] = 1
        for a in "asdfghjkl":
            alphabets[a] = 2
        for a in "zxcvbnm":
            alphabets[a] = 3
        
        result = []
        for word in words:
            num = alphabets[word[0].lower()]
            is_valid = True
            for i in range(1, len(word)):
                if alphabets[word[i].lower()] != num:
                    is_valid = False
                    
            if is_valid: result.append(word)
                
        return result
                
                    
            
                
        