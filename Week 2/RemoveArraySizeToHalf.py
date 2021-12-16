from typing import Collection


class Solution:
    def minSetSize(self, arr):
        freq = Collection.Counter(arr)
        
        uniqueList = list(set(arr))        
        uniqueList.sort(key=lambda x: freq[x])
        
        removed = 0
        count = 0
        n = len(arr)
        for i in reversed(uniqueList):
            removed += freq[i]
            count += 1
            if (removed >= n//2):
                return count