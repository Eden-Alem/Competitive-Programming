class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique = set()
        for i in range(len(s)-k+1):
            unique.add(s[i:i+k])
             
        return len(unique) == 2**k