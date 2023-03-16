class Solution:
    def maxLength(self, arr: List[str]) -> int:
        chars = set()
        
        def unique(chars, string):
            count = Counter(chars) + Counter(string)
            return max(count.values()) > 1
        
        def backtrack(i):
            if i >= len(arr):
                return len(chars)
            
            result = 0
            if not unique(chars, arr[i]):
                for a in arr[i]:
                    chars.add(a)
                    
                result = backtrack(i+1)
                
                for a in arr[i]:
                    chars.remove(a)
                  
            
            return max(result, backtrack(i+1))
        
        return backtrack(0)