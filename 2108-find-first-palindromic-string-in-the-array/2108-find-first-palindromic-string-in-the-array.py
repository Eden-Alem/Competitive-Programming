class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindromic(word):
                return word
            
        return ""
        
        
    def isPalindromic(self, word):
        reverse_word = word[::-1]
        return word == reverse_word