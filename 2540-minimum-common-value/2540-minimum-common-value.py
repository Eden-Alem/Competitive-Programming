class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_uniq = set(nums2)
        
        for n in nums1:
            if n in nums2_uniq:
                return n
        
        return -1