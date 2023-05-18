class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bin_n = bin(n)
        isEven = True
        count = [0, 0]
        
        arr = bin_n[2:][::-1]
        for b in arr:
            if isEven:
                if b == '1':
                    count[0] += 1
                isEven = False
                    
            else:
                if b == '1':
                    count[1] += 1
                    
                isEven = True
                
        return count
                    