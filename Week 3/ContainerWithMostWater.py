class Solution:
    def maxArea(self, height) -> int:
        leftConstraint = 0
        rightConstraint = len(height) - 1
        maxArea = 0
        while (leftConstraint < rightConstraint):
                maxArea = max(maxArea, ((rightConstraint - leftConstraint) * min(height[leftConstraint], height[rightConstraint])) )
                if (height[leftConstraint] > height[rightConstraint]):
                    rightConstraint -= 1
                else:
                    leftConstraint += 1
                    
        return maxArea