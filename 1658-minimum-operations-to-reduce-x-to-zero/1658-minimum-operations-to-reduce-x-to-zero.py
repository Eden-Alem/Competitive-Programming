class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left = 0        
        size = float("-inf")
        tempSum = 0
        target = sum(nums) - x
        
        for right in range(n):
            tempSum += nums[right]
            
            while tempSum > target and left <= right:
                tempSum -= nums[left]
                left += 1
                
            if tempSum == target:
                size = max(size, right-left+1)
                
        return n - size if size != float("-inf") else -1
        