class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for log in logs:
            list_log = log.split(" ")
            if list_log[1].isdigit():
                digits.append(log)
            else:
                letters.append(([list_log[0]], list_log[1:]))
        
        sorted_letters = sorted(letters, key=lambda x:(x[1],x[0]))
        
        result = []
        
        for identifier, letter in sorted_letters:
            identifier.extend(letter)
            result.append(" ".join(identifier))
            
        result.extend(digits)
        
        return result
        
        
        