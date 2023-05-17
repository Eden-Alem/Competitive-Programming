class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)
        
        bin_comp = 0
        arr = bin_num[2:][::-1]
        
        for i, n in enumerate(arr):
            if n == '0':
                bin_comp += (2 ** i)
                
        return bin_comp