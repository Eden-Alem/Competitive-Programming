class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            count += self.binarySearch(row)
            
        return count
            
    def binarySearch(self, row):
        left = 0
        right = len(row) - 1
        start = len(row)
        while (left <= right):
            mid = (left + right)//2
            if (row[mid] < 0):
                start = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return len(row) - start
        