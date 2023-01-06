class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Index = { n:i for i, n in enumerate(nums1) }
        result = [-1] * len(nums1)

        monoStack = []
        for i in range(len(nums2)):
            num = nums2[i]
            while monoStack and num > monoStack[-1]:
                index = nums1Index[monoStack.pop()]
                result[index] = num

            if num in nums1Index:
                monoStack.append(num)

        return result