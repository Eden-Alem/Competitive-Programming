class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dfs(string):
            chars = set(string)
            if len(string) < 2:
                return ""
            
            for i in range(len(string)):
                if not(string[i].upper() in chars and string[i].lower() in chars):
                    left_string = dfs(string[:i])
                    right_string = dfs(string[i+1:])
                    
                    return right_string if len(right_string) > len(left_string) else left_string
                
            return string
        
        return dfs(s)
        