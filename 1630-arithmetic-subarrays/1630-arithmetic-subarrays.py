class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        
        for i in range(len(l)):
            arr = sorted(nums[l[i]:r[i]+1])
            result.append(self.isArithmetic(arr))
            
        return result
    
    def isArithmetic(self, arr):
        diff = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i] != diff): return False 
        
        return True

        