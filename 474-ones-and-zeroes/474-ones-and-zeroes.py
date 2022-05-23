class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.zerosAndOnes(0, strs, m, n, {})
        
    def zerosAndOnes(self, i, strs, zeros, ones, memo):
        if (i == len(strs)) or (zeros + ones == 0):
            return 0
                
        if (zeros, ones, i) in memo:
            return memo[(zeros, ones, i)]
        
        numberOfZeros = 0
        for s in strs[i]:
            if s == "0":
                numberOfZeros += 1                
        numberOfOnes = len(strs[i]) - numberOfZeros
        
        pick = 0
        if zeros >= numberOfZeros and ones >= numberOfOnes:
            pick = self.zerosAndOnes(i+1, strs, zeros - numberOfZeros, ones - numberOfOnes, memo) + 1
            
        dontPick = self.zerosAndOnes(i+1, strs, zeros, ones, memo) 
        
        memo[(zeros, ones, i)] = max(pick,dontPick)
        
        return memo[(zeros, ones, i)]
            