class Solution:
    def __init__(self):
        self.result = []
        
    def letterCombinations(self, digits: str) -> List[str]:
        mappedNumbers = {
            "2" : {"a","b","c"},
            "3" : {"d",'e','f'},
            "4" : {'g','h','i'},
            "5" : {'j','k','l'},
            "6" : {'m','n','o'},
            "7" : {'p','q','r','s'},
            "8" : {'t','u','v'},
            "9" : {'w','x','y','z'}
        }
        
        if digits:
            self.backtrack(mappedNumbers, 0, digits, "")
            
        return self.result
        
    def backtrack(self, mapped, i, digits, builtStr):
        if i >= len(digits):
            self.result.append(builtStr)
            return
        
        for c in mapped[digits[i]]:
            self.backtrack(mapped, i+1, digits, builtStr+c)
        
