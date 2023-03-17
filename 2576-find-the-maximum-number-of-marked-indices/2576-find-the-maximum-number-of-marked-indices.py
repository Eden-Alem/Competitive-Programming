class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        mark = 0
        mid = n // 2
        left, right = 0, mid

        while left < mid and right < n:
            if (2 * nums[left] <= nums[right]):
                mark += 2
                left += 1
            right += 1

        return mark