from typing import Collection


class Solution:
    def findOriginalArray(self, changed):
        frequencyDict = Collection.Counter(changed)        
        result = []
        
        if (len(changed) % 2 != 0): return []
        
        for num in sorted(frequencyDict.keys()):
            while (num == 0 and frequencyDict[num] >= 2):             
                frequencyDict[num] -= 2
                result.append(num)
                
            
            while (num > 0 and frequencyDict[num] and frequencyDict[num * 2]):
                frequencyDict[num] -= 1
                frequencyDict[num * 2] -= 1
                result.append(num) 
                
        
        return result if len(changed)//2 == len(result) else []