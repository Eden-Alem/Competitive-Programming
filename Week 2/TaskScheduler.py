from typing import Collection


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        frequencyDict = Collection.Counter(tasks)
        
        result = []
        while len(frequencyDict):
            tempRes = [None] * (n+1)
            temp = dict(frequencyDict.most_common(n + 1))
                
            j = 0
            for i in temp:
                tempRes[j] = i
                frequencyDict[i] -= 1
                j += 1
                if (frequencyDict[i] == 0):                   
                    del frequencyDict[i] 
                    
            result.extend(tempRes)
            
        while result and result[-1] is None:
            del result[-1]
            
        return len(result)
