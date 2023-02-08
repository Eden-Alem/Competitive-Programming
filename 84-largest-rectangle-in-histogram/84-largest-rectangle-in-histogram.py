class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        monoStack = [-1]
        maxArea = 0
        for i in range(len(heights)):
            while (heights[i] < heights[monoStack[-1]]):
                height = heights[monoStack.pop()]
                width = i - monoStack[-1] - 1
                maxArea = max(maxArea, height * width)
            monoStack.append(i)
        return maxArea
    