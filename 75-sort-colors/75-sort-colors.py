class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n):
            curr = nums[i]
            
            j = i - 1
            while (j >= 0 and curr < nums[j]):
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = curr
            
        print(nums)
        