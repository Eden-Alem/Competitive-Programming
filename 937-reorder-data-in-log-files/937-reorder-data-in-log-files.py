class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for log in logs:
            if log[-1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        sortedLetters = []
        for letter in letters:
            index = letter.index(" ")
            sortedLetters.append((letter[index+1:], letter[:index]))
            
        sortedLetters.sort()
        result = []
        for sl in sortedLetters:
            result.append(sl[1] + " " + sl[0])
            
        result.extend(digits)
        
        return result
        