class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        minEle = nums[0:2]
        minEle.append(nums[-1])
        
        maxEle = nums[n-3 : n]
        return max(minEle[0] * minEle[1] * minEle[2], maxEle[0] * maxEle[1] * maxEle[2])
        