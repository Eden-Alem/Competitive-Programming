class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]* (2**n)
        for i in range(n):
            temp = [0] * 2**i + [1] *  2**i
            while len(temp) < 2**n:
                temp = temp + list(reversed(temp))
            
            # result[0] = temp[0] xor result[0]
            # result[1] = temp[1] xor result[1]
            for j in range(len(temp)):
                result[j] = temp[j]<<i ^ result[j]
             
        return result
            
            
            
        