class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        result = []
        
        for i in range(n):
            iNum = nums[i]            
            if (i > 0 and iNum == nums[i-1]):
                continue
            
            l, r = i + 1, n - 1            
            while (l < r):
                tempSum = iNum + nums[l] + nums[r]
                if (tempSum > 0):
                    r -= 1
                elif (tempSum < 0):
                    l += 1
                else:
                    result.append([iNum, nums[l], nums[r]])
                    r -= 1
                    
                    while (nums[r] == nums[r+1] and l < r):
                        r -= 1
                    
        return result
            