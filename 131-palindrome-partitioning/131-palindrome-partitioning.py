class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(string):
            reverse = string[::-1]
            return string == reverse
        
        result = []
        palindrome = []
        def backtrack(i):
            if i >= len(s):
                result.append(palindrome.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    palindrome.append(s[i:j+1])
                    backtrack(j+1)
                    palindrome.pop()
            
        backtrack(0)
        return result
       
    
            
        
        
        
        
        