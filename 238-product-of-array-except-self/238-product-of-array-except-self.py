class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftRight = [1]
        
        for i in range(n):
            leftRight.append(leftRight[-1] * nums[i])    
        
        rightLeft = [1]
        
        for j in range(n-1,-1,-1):
            rightLeft.append(rightLeft[-1] * nums[j])
            
        rightLeft.reverse()
        
        result = []
        
        print(leftRight)
        print(rightLeft)
        
        for k in range(n):
            result.append(rightLeft[k+1] * leftRight[k])
            
        return result