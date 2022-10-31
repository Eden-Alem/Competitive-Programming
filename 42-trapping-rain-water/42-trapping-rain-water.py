class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)        
        left = 0
        right = n - 1
        
        maxLeft = height[left] 
        maxRight = height[right]
        
        blocks = 0
        while (left < right):
            if (maxRight < maxLeft):
                right -= 1
                maxRight = max(maxRight, height[right])
                blocks += (maxRight - height[right])
                
            else:
                left += 1
                maxLeft = max(maxLeft, height[left])
                blocks += (maxLeft - height[left])
                
        return blocks
                
        
        