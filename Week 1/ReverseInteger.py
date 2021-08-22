class Solution:
    def reverse(self, x: int) -> int:
        stringified = str(x)
        if (stringified[0] == '-'):
            value = stringified[:0:-1]
            if (-2**31 <= int('-' + value)):
                return int('-' + value)
            else:
                return 0
        else:
            value = stringified[::-1]
            if (int(value) <= 2**31 - 1):
                return int(value)
            else:
                return 0

print(Solution().reverse(-1629))