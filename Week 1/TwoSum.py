from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()
        for i in range(len(nums)):
            if nums[i] in hashTable:
                return (nums.index(hashTable[nums[i]]), i)
            else:
                hashTable[target - nums[i]] = nums[i]

print(Solution().twoSum([2,4,6,8], 6))
                