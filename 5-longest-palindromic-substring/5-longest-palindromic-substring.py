class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        palindromeLen = 0
        result = ""
        
        for i in range(n):
            left = i
            right = i
            while (left >= 0 and right < n) and s[left] == s[right]:
                if (right-left+1) > palindromeLen:
                    result = s[left:right+1]
                    palindromeLen = right-left+1
                left -= 1
                right += 1
                
            
            left = i
            right = i+1
            while (left >= 0 and right < n) and s[left] == s[right]:
                if (right-left+1) > palindromeLen:
                    result = s[left:right+1]
                    palindromeLen = right-left+1
                left -= 1
                right += 1
                
        return result
        
                
        