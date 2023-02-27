class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        while n > 1:
            new_nums = [0] * (n-1)
            for i in range(n-1):
                new_nums[i] = (nums[i] + nums[i+1]) % 10
                
            nums = new_nums
            n-=1
            
        return nums[0]
        