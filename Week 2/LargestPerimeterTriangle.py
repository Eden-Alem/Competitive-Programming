class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #         nums.sort()
        #         value = (itertools.combinations(nums, 3))

        #         lists = []
        #         for i in value:
        #             newlist = sorted(i)
        #             if newlist not in lists:
        #                 lists.append(newlist)

        #         for i in (lists[::-1]):
        #             if (self.triangleBuilder(list(i))):
        #                 return sum(i)
        #         return 0

        #     def triangleBuilder(self, triangle):
        #         triangle.sort()
        #         if (triangle[0] + triangle[1] > triangle[2] and triangle[1] + triangle[2] > triangle[0] and triangle[0] + triangle[2] > triangle[1]):
        #             return True
        #         else:
        #             return False
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if(i >= 0):
                if (nums[i] + nums[i + 1] > nums[i + 2]):
                    return nums[i] + nums[i + 1] + nums[i + 2]
        return 0