from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        permutatedNums = []
        for i in range(len(nums)):
            permutatedNums.append(nums[nums[i]])
        return permutatedNums

print(Solution().buildArray([0,1,2,5,4,3]))
        