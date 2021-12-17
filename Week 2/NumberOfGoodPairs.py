from typing import Collection


class Solution:
    def numIdenticalPairs(self, nums):
        frequencyDict = Collection.Counter(nums)
        
        result = 0
        for i in frequencyDict.keys():
            result += (frequencyDict[i]*(frequencyDict[i]-1))//2
        return result
        