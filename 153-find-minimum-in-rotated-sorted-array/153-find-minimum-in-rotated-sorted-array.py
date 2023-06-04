class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n-1
        while (left <= right):
            mid = (left + right)//2
            if (nums[mid] >= nums[0]):
                left = mid + 1
            else:
                right = mid -1

        return nums[0] if (left >= n) else nums[left]