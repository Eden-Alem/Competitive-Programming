class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        
        p1, p2 = 0, 0
        
        while p1 <= n1-1 and p2 <= n2-1:
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            
            elif nums1[p1] < nums2[p2]:
                p1 += 1
                
            else:
                p2 += 1
        
        return -1