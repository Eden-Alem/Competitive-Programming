class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if self.checker(s):
            return 1
        return 2
    
    def checker(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1
            
        return True