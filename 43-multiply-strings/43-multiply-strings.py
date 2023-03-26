class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1, num2 = num1[::-1], num2[::-1]
        n1, n2 = len(num1), len(num2)
        
        result = [0] * (n1 + n2)
        
        for i in range(n1):
            for j in range(n2):
                product = int(num1[i]) * int(num2[j])
                
                result[i + j] += product
                result[i + j + 1] += (result[i + j] // 10)
                
                result[i + j] = result[i + j] % 10
                
        result.reverse()
        k = 0
        
        while k < len(result) and result[k] == 0:
            k+=1
            
        return "".join(map(str, result[k:]))