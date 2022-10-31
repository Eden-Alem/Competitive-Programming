class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        leftCons = 0
        rightCons = n - 1
        
        maxarea = float("-inf")
        
        while leftCons < rightCons:
            maxarea = max(maxarea, (rightCons - leftCons) * min(height[rightCons], height[leftCons]))
            
            if (height[rightCons] > height[leftCons]):
                leftCons += 1
                
            else:
                rightCons -= 1
                
        return maxarea