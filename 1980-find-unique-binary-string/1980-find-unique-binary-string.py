class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        appeared = set(nums)
        
        def backtrack(i, path):
            if i == len(nums):
                string = "".join(path)
                return string if string not in appeared else None
            
            
            path[i] = "1"
            result = backtrack(i+1, path)
            if result:
                return result
            
            path[i] = "0"
            result = backtrack(i+1, path)
            
            if result:
                return result
            
        return backtrack(0, ["0"]*len(nums))

        