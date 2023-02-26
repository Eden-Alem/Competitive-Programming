class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [0] * n
        if s[0] == '*':
            prefix[0] = 1
        for i in range(1, n):
            if s[i] == '*':
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]

        left = [0] * n
        right = [0] * n
        
        left[0] = -1 if s[0] == "*" else 0
        
        for i in range(1, n):
            if s[i] != '*':
                left[i] = i
            else:
                left[i] = left[i-1]

        right[n-1] = -1 if s[n-1] == "*" else n-1
        
        for i in range(n-2, -1, -1):
            if s[i] == '*':
                right[i] = right[i+1]
            else:
                right[i] = i

        result = []
        for start, end in queries:
            l = right[start]
            r = left[end]
            if l == -1 or r == -1 or l >= r:
                result.append(0)
                continue
                
            result.append(prefix[r] - prefix[l])

        return result
