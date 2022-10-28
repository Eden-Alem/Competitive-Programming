class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for val in s:
            if val.isalnum():
                string += val.lower()
        return self.palindromeChecker(string)
        
    def palindromeChecker(self, s):
        n = len(s)
        left = 0
        right = n-1
        
        while (left < right):
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
            
        return True
        