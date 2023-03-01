class Solution:
    def minSwaps(self, s: str) -> int:
        openn, close = 0, 0
        
        arr = [c for c in s]
        n = len(arr)
        swaps = 0
        right = n-1
        left = 0
        
        while left < right:
            if arr[left] == '[':
                openn += 1
                
            elif arr[left] == ']':
                close += 1
                
            if close > openn:
                while arr[right] != '[':
                    right -= 1
                
                arr[left], arr[right] = arr[right], arr[left]
                close -= 1
                openn += 1
                swaps += 1
                
            left += 1
                
        return swaps  
    
      
            
            
        