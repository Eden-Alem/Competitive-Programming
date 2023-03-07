class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        
        def lessThan(num):
            count = 0
            l, r = 0, n-1
            
            while l < r:
                while l < r and nums[l] + nums[r] >= num:
                    r -= 1
                  
                count += (r-l)
                l += 1
                
            return count
        
        lessThanUpper = lessThan(upper+1)
        lessThanLower = lessThan(lower)
        
        return lessThanUpper - lessThanLower