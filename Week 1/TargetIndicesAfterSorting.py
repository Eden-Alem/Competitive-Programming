class Solution:
    def targetIndices(self, nums, target: int):
        for i in range(len(nums)):
            minimum = i
            for j in range(i + 1, len(nums)):
                if (nums[minimum] > nums[j]):
                    minimum = j
                    
            nums[i], nums[minimum] = nums[minimum], nums[i]
            
        return [i for i in range(len(nums)) if nums[i] == target]