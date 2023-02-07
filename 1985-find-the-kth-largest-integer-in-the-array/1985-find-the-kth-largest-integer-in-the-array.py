class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = len(nums)
        for i in range(n):
            nums[i] = int(nums[i])
            
        nums.sort()
        return str(nums[-k])
        