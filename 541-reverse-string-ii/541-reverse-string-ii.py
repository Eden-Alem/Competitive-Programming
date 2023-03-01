class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        n = len(arr)
        
        for i in range(0, n, 2*k):
            arr[i:i+k] = reversed(arr[i:i+k])
            
        return "".join(arr)
            
        