from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2Sorted = []
        for i in arr2:
            if (i in arr1):
                for j in range(arr1.count(i)):
                    arr2Sorted.append(i)
                    arr1.remove(i)
        arr1.sort()
        if (len(arr1) > 0):
            arr2Sorted.extend(arr1)
        return arr2Sorted

print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))