class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        
        result = []
        for n in set_nums1:
            if n in set_nums2:
                result.append(n)
                
        return result
        