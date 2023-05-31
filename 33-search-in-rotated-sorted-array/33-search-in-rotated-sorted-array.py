class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1
        while (left <= right):
            mid = (left + right)//2
            if (nums[mid] >= nums[0]):
                left = mid + 1
            else:
                right = mid - 1

        leftLeft = 0
        rightLeft = left - 1
        while (leftLeft <= rightLeft):
            mid = (leftLeft + rightLeft)//2
            if (nums[mid] > target):
                rightLeft = mid - 1
            elif (nums[mid] < target):
                leftLeft = mid + 1
            else:
                return mid

        leftRight = left
        rightRight = n - 1
        while (leftRight <= rightRight):
            mid = (leftRight + rightRight)//2
            if (nums[mid] > target):
                rightRight = mid -1
            elif (nums[mid] < target):
                leftRight = mid + 1
            else:
                return mid

        return -1


