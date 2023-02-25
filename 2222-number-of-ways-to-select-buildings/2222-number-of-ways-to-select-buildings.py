class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = [0]
        zeros = [0]
        
        for char in s:
            if char == "0":
                zeros.append(zeros[-1] + 1)
                ones.append(ones[-1])
                
            else:
                ones.append(ones[-1] + 1)
                zeros.append(zeros[-1])
                
        n = len(s)
        ways = 0
        for i in range(n-1):
            if s[i] == "0":
                ways += ((ones[-1]-ones[i+1]) * (ones[i+1]))
            else:
                ways += ((zeros[-1]-zeros[i+1]) * (zeros[i+1]))
            
        return ways