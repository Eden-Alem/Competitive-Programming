from typing import Collection


class Solution:
    def maxOperations(self, nums, k: int) -> int:
        frequencyDict = Collection.Counter(nums)

        count = 0
        for num in frequencyDict.keys():
            while (num == k-num and frequencyDict[num] >= 2):             
                frequencyDict[num] -= 2
                count += 1
            
            while (num != k-num and frequencyDict[num] and frequencyDict[k - num]):
                frequencyDict[num] -= 1
                frequencyDict[k - num] -= 1
                count += 1
    
        return count
