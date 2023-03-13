class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        prefix = 0
        max_score = 0

        for num in reversed(nums):
            prefix += num

            if prefix > 0:
                max_score += 1


        return max_score