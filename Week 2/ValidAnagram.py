class Solution(object):
    def isAnagram(self, s, t):
        arrayOfS = list(s)
        if len(s) == len(t):
            for i in range(len(s)):
                if t[i] not in arrayOfS:
                    return False
                arrayOfS.remove(t[i])
            return True
        return False

print(Solution().isAnagram("dance", "andce"))