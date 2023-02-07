class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        
        if n % 2 != 0:
            return []
        
        freq = Counter(changed)
        
        result = []
        for num in sorted(freq):
            while (num == 0 and freq[num] >= 2):             
                freq[num] -= 2
                result.append(num)
                
            
            while (num > 0 and freq[num] and freq[num * 2]):
                freq[num] -= 1
                freq[num * 2] -= 1
                result.append(num) 
                
        return result if n // 2 == len(result) else []
                
            
            
        